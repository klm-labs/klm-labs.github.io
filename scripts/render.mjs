// Existing browser tooling can be supplied by absolute path; never installs packages.
import { createRequire } from 'node:module';
import { constants } from 'node:fs';
import { access, mkdir, writeFile } from 'node:fs/promises';
import { isAbsolute } from 'node:path';
const require = createRequire(import.meta.url);
const required = ['PLAYWRIGHT_PATH', 'CHROME_PATH', 'RENDER_DIR'];
const missing = required.filter(name => !process.env[name]?.trim());
if (missing.length) throw new Error(`Missing required environment variables: ${missing.join(', ')}. See README.md for browser-check usage.`);
for (const name of required) {
  if (!isAbsolute(process.env[name])) throw new Error(`${name} must be an absolute path.`);
}
let chromium;
try {
  ({ chromium } = require(process.env.PLAYWRIGHT_PATH));
  if (typeof chromium?.launch !== 'function') throw new Error();
} catch {
  throw new Error('PLAYWRIGHT_PATH must point to a loadable Playwright module with Chromium support.');
}
try {
  await access(process.env.CHROME_PATH, constants.X_OK);
} catch {
  throw new Error('CHROME_PATH must point to an existing executable Chrome or Chromium browser.');
}
const output = process.env.RENDER_DIR;
try {
  await mkdir(output, { recursive: true });
  await access(output, constants.W_OK);
} catch {
  throw new Error('RENDER_DIR must be a writable output directory, or a directory that can be created.');
}
const browser = await chromium.launch({
  executablePath: process.env.CHROME_PATH,
  headless: true,
  args: ['--no-sandbox'],
});
const base = process.env.SITE_URL || 'http://127.0.0.1:8765';
const pages = [['studio', '/'], ['app', '/invoice-creator/'], ['privacy', '/invoice-creator/privacy/'], ['terms', '/invoice-creator/terms/'], ['support', '/invoice-creator/support/']];
const findings = [];
try {
  for (const viewport of [{ width: 390, height: 844 }, { width: 1440, height: 900 }]) {
    const context = await browser.newContext({ viewport, deviceScaleFactor: 1, reducedMotion: 'reduce' });
    for (const [name, path] of pages) {
      const page = await context.newPage();
      const errors = [];
      const requests = [];
      page.on('pageerror', error => errors.push(error.message));
      page.on('console', message => { if (message.type() === 'error') errors.push(message.text()); });
      page.on('request', request => requests.push(request.url()));
      page.on('requestfailed', request => errors.push(`${request.failure()?.errorText} ${request.url()}`));
      page.on('response', response => { if (response.status() >= 400) errors.push(`${response.status()} ${response.url()}`); });
      const response = await page.goto(base + path, { waitUntil: 'networkidle' });
      await page.evaluate(() => document.fonts.ready);
      // Load below-fold lazy images before capturing the full page.
      await page.evaluate(async () => {
        const images = [...document.images];
        images.forEach(image => { image.loading = 'eager'; });
        await Promise.all(images.map(image => image.decode().catch(() => {})));
      });
      const metrics = await page.evaluate(() => {
        const text = [];
        const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
        while (walker.nextNode()) {
          const node = walker.currentNode;
          const element = node.parentElement;
          if (!node.textContent.trim() || !element?.checkVisibility() || element.closest('script,style')) continue;
          const range = document.createRange();
          range.selectNodeContents(node);
          if (![...range.getClientRects()].some(rect => rect.width && rect.height)) continue;
          text.push({
            text: node.textContent.trim().slice(0, 100),
            fontSize: parseFloat(getComputedStyle(element).fontSize),
            bodyCopy: Boolean(element.closest('p:not(.eyebrow), .prose, .studio-card-copy small')),
          });
        }
        return {
          width: innerWidth,
          scrollWidth: document.documentElement.scrollWidth,
          h1s: document.querySelectorAll('h1').length,
          brokenImages: [...document.images].filter(i => !i.complete || !i.naturalWidth).map(i => i.src),
          missingAlt: [...document.images].filter(i => !i.hasAttribute('alt')).map(i => i.src),
          externalResources: performance.getEntriesByType('resource').map(r => r.name).filter(url => new URL(url).origin !== location.origin),
          minimumFontPx: Math.min(...text.map(item => item.fontSize)),
          minimumBodyFontPx: Math.min(...text.filter(item => item.bodyCopy).map(item => item.fontSize)),
          smallText: text.filter(item => item.fontSize < 12),
          smallMobileBodyText: innerWidth <= 760 ? text.filter(item => item.bodyCopy && item.fontSize < 16) : [],
        };
      });
      metrics.runtimePaths = [...new Set(requests.map(url => new URL(url).pathname))].sort();
      metrics.sourceRequests = metrics.runtimePaths.filter(path => /^\/(?:README\.md|CLAUDE\.md|(?:docs|scripts|data|content|templates)(?:\/|$))/.test(path));
      if (process.env.AXE_PATH) {
        await page.addScriptTag({ path: process.env.AXE_PATH });
        const audit = await page.evaluate(async () => window.axe.run(document, { runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa'] } }));
        metrics.accessibilityViolations = audit.violations.map(v => ({ id: v.id, impact: v.impact, nodes: v.nodes.map(n => n.target) }));
        if (metrics.accessibilityViolations.length) throw new Error(JSON.stringify({ path, viewport, violations: metrics.accessibilityViolations }));
      }
      if (response.status() !== 200 || metrics.scrollWidth > viewport.width || metrics.h1s !== 1 || metrics.brokenImages.length || metrics.missingAlt.length || metrics.externalResources.length || metrics.sourceRequests.length || metrics.smallText.length || metrics.smallMobileBodyText.length || errors.length) {
        throw new Error(JSON.stringify({ path, viewport, metrics, errors }));
      }
      const file = `${output}/${name}-${viewport.width}x${viewport.height}.png`;
      await page.screenshot({ path: file, fullPage: true });
      if (name === 'app') {
        const apple = page.locator('.store-coming-soon');
        if (await apple.evaluate(e => e.tagName !== 'DIV' || e.closest('a,button') !== null || e.tabIndex >= 0)) throw new Error('Coming soon must be non-interactive');
        if (await page.locator('.store-badge.google_play').getAttribute('href') !== 'https://play.google.com/store/apps/details?id=com.klmlabs.invoicecreator') throw new Error('Wrong Play URL');
        const next = page.locator('.carousel-next');
        await next.click();
        if (await page.locator('.screenshot-track').evaluate(e => e.scrollLeft) <= 0) throw new Error('Carousel next did not scroll');
        await page.locator('.screenshot-track').focus();
        await page.keyboard.press('ArrowLeft');
        if (await page.locator('.screenshot-track').evaluate(e => e.scrollLeft) > 2) throw new Error('Carousel keyboard navigation failed');
      }
      if (errors.length) throw new Error(JSON.stringify({ path, viewport, errors }));
      findings.push({ page: path, viewport, status: response.status(), ...metrics, errors, file });
      console.log(`PASS ${path} ${viewport.width}×${viewport.height}`);
      await page.close();
    }
    await context.close();
  }
  // Native scrolling and links still work when JavaScript is unavailable.
  const noJS = await browser.newContext({ javaScriptEnabled: false, viewport: { width: 390, height: 844 } });
  const page = await noJS.newPage();
  await page.goto(base + '/invoice-creator/');
  if (await page.locator('.screenshot-card').count() !== 5 || await page.locator('.store-badge').count() !== 1) throw new Error('No-JS content missing');
  await noJS.close();
  await writeFile(output + '/checks.json', JSON.stringify(findings, null, 2) + '\n');
} finally {
  await browser.close();
}
