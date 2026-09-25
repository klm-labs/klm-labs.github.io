# KLM Labs app site

Public site: **https://klm-labs.github.io**. GitHub Pages publishes committed files
from **`main`, repository root**. `.nojekyll` keeps Pages from interpreting the
generated HTML. There is no backend, CDN dependency, runtime package, or site analytics.

## Architecture

| Source | Purpose |
| --- | --- |
| `data/apps/<slug>.json` | One app record: copy, store state, screenshots, release, data safety, contact and metadata |
| `content/<slug>/{privacy,terms,support}.md` | The app’s reviewed policy and support text |
| `<slug>/icon.png`, `favicon.png`, `screenshots/` | Real app assets; all self-hosted |
| `templates/` | One shared shell, app listing, studio index and document layout |
| `assets/site.css`, `assets/site.js` | Shared design system and progressive carousel enhancement |
| `scripts/build.py` | Deterministic generator: HTML, social PNGs, sitemap and robots.txt |
| `scripts/check.py`, `scripts/render.mjs` | Route, content, metadata and browser checks |

The shared layout generates `/`, `/<slug>/`, and `/<slug>/{privacy,terms,support}/`.
**Edit sources, then rebuild; never hand-edit generated HTML.** The generator has
one pinned dependency, Pillow, used for social images. Python 3.12+ is required.
The Markdown subset supports paragraphs, `##`/`###` headings, bullet lists, tables,
links, bold, italic and inline code. A source `#` title is replaced by the layout’s
single page heading. Separate paragraphs with a blank line. Raw HTML is escaped.

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/build.py
python3 scripts/check.py
python3 -m http.server 8765 --bind 127.0.0.1
```

Run the builder a second time and confirm no generated diff: output is reproducible
with the pinned dependency and committed fonts. Commit the generated files alongside
the source change. The TTFs are used only by the image generator; browsers download
the smaller WOFF2 subsets. Font licenses and store badge provenance are in
[`assets/README.md`](assets/README.md).

## Add a new app

1. Add `data/apps/<slug>.json`, using the Invoice Maker record
   (`invoice-creator.json`) as the schema. Supply factual copy and store status.
   The `slug` must match the new directory name. Replace every app-specific
   value, including `bundle_id`, platforms, category, developer, contact and
   data-safety entries. Do not advertise an app whose details have not been
   verified.
2. Put its icon and favicon at the paths in that record. Put real captures in
   `<slug>/screenshots/`; provide file, title, caption, alt text, dimensions and
   source provenance for every entry. At least one screenshot is required.
3. Add `content/<slug>/privacy.md`, `terms.md` and `support.md`. Check privacy
   against that app’s implementation and current store declarations. Do not copy
   Invoice Maker’s data practices into an unrelated app.
4. Rebuild. Its listing, three resource pages, studio card, social image and
   sitemap entries are generated automatically. No HTML or CSS copying is needed.
5. Check links, inspect desktop/mobile renders, commit, push and verify live.

## Flip a store button live

Each record has `stores.app_store` and `stores.google_play`, each with `url`
(`null` or an HTTPS URL) and `live` (boolean). `live: true` requires a valid URL
and renders an official badge link. `live: false` renders plain **Coming soon**
text in a non-interactive element, even if a future URL is already known.
The Apple artwork is used only when the App Store link is live.

For **Invoice Maker**, change these exact entries in
[`data/apps/invoice-creator.json`](data/apps/invoice-creator.json):

- **App Store, line 16:** once App Store Connect → app → App Information supplies
  the numeric Apple ID and its listing is publicly available, replace
  `"app_store": { "url": null, "live": false }` with
  `"app_store": { "url": "https://apps.apple.com/app/id<ACTUAL_NUMERIC_ID>", "live": true }`.
  Replace the entire placeholder with the real digits. Do not use a bundle ID,
  TestFlight URL, search URL or fabricated numeric ID.
- **Google Play, line 17:** the final canonical URL and `live: true` are already
  set, explicitly requested by the founder while the app is in closed testing.
  **No button change is required at production launch.** The public URL returned
  404 on 2026-09-11; that is why the nearby availability copy explains testing.
- **Line 19, `availability`:** update this sentence as each store actually launches.
  Also change `release.label` from “First release · in testing” when appropriate.

For later apps use `live: false` until the store listing is publicly usable.
Rebuild, preview both button states, publish and check the exact outbound URLs.
The generator validates canonical Play URLs and numeric Apple listing URLs.

## Refresh screenshots

Only use captures of the real app. Prefer the cleanest current release candidate;
avoid errors, keyboards, junk test records and the Invoice Maker Preview screen
until its layout fixes have been verified. Do not draw, retouch or synthesize app UI.

Replace files in `<slug>/screenshots/` and edit only that app’s `screenshots` list
(order, captions, alt text, dimensions and provenance). The initial set is 576 × 1280,
WebP quality 86, about **105 KB total** for five images. Refresh a file with:

```sh
.venv/bin/python scripts/prepare-screenshot.py /absolute/path/to/capture.png invoice-creator/screenshots/01-invoices.webp
```

This preserves the entire capture, resizes to fit 576 × 1280 without stretching,
and writes compressed WebP. Use the printed dimensions in the data. Rebuild and
inspect every frame at both target viewports. Swapping screenshot files does not
require changing templates or CSS. Do not store test logs, personal data or secrets
alongside public screenshots.

## Verify and publish

The registered URLs must continue returning HTTP 200:

- `/`
- `/invoice-creator/`
- `/invoice-creator/privacy/`
- `/invoice-creator/terms/`
- `/invoice-creator/support/`

The app was renamed from Invoice Creator to Invoice Maker on 2026-09-25. Its slug,
file names and these paths stay `invoice-creator`, because the stores already link
to them.

With the local server running, the browser check saves full-page PNGs at
390 × 844 and 1440 × 900 viewport sizes. Supply these three required environment
variables as absolute paths; there are no machine-specific defaults:

- `PLAYWRIGHT_PATH`: an existing, loadable Playwright module directory.
- `CHROME_PATH`: an existing Chrome or Chromium executable.
- `RENDER_DIR`: a writable artifact directory; created if it does not exist.

```sh
PLAYWRIGHT_PATH=/absolute/path/to/node_modules/playwright \
CHROME_PATH=/absolute/path/to/chrome \
RENDER_DIR=/absolute/path/to/render-artifacts \
node scripts/render.mjs
```

Missing variables, invalid module/browser paths and unusable output directories
produce explicit errors. The script installs nothing. Use existing tooling or
install it outside the read-only app repository. `SITE_URL` optionally overrides
`http://127.0.0.1:8765`, for example `SITE_URL=https://klm-labs.github.io` for live
checks. To run WCAG A/AA checks, supply `AXE_PATH` pointing to an installed
`axe-core/axe.min.js` outside the app repository.

Files are `{studio,app,privacy,terms,support}-{390x844,1440x900}.png` plus
`checks.json`. These are verification artifacts, not published assets.

Inspect the images. The checks cover local link targets and anchors, canonical and
social metadata, page overflow, missing images, external runtime requests, console
errors, failed requests, computed text sizes (at least 12 px everywhere and 16 px
for mobile body copy), store-link/coming-soon behavior, reduced-motion carousel
controls and the no-JavaScript content. Runtime requests must not load the source
paths excluded in `robots.txt`: `README.md`, `CLAUDE.md`, `docs/`, `scripts/`,
`data/`, `content/` and `templates/`. These exclusions guide crawlers; the files
remain publicly served by Pages. `check.py` also catches the FB-066
analytics-control regression.

Commit source and generated output to `main`, then push to `origin main`.
Include any commit trailers requested for the publishing task.

Poll `gh api repos/klm-labs/klm-labs.github.io/pages/builds/latest` no faster than
every 20 seconds, for up to ten minutes. Confirm `status: built` and `commit`
equals the pushed SHA. Then curl all registered paths on the public origin,
expect 200, verify the deployed content and assets, and check the live privacy
page includes automatic keyed-native collection and the web/key-free exclusion.
Search the live policy for `opt out`, `opt-out`, `turn off`, `disable`,
`choose whether` and `preference`: it must not resurrect an analytics control.

## Policy review and remaining store work

The app repository is **read-only** for this site task. FB-066 review evidence and
the exact source-policy corrections to reconcile back into that repository are in
[`docs/fb-066-review.md`](docs/fb-066-review.md). The app’s current draft already
describes always-on analytics; the old published HTML was the severe mismatch.
Store console updates, processor retention settings and the Apple ID are outside
this site repository. Do not label them verified merely because the website is live.
