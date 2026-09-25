#!/usr/bin/env python3
"""Render the complete Pages site from shared templates and per-app content."""
import hashlib
import html
import json
import re
from pathlib import Path
from string import Template

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
ORIGIN = 'https://klm-labs.github.io'
LABELS = {'privacy': 'Privacy policy', 'terms': 'Terms of use', 'support': 'App support'}
DECKS = {
    'privacy': 'What stays on your device, what is collected, and how to get in touch.',
    'terms': 'The terms that apply when you use the app.',
    'support': 'A little help, so you can get back to work.',
}
PATHS = {
    'arrow_right': '<path d="M4 12h16m-6-6 6 6-6 6"/>',
    'arrow_left': '<path d="M20 12H4m6-6-6 6 6 6"/>',
    'arrow_down': '<path d="M12 4v16m-6-6 6 6 6-6"/>',
    'document': '<path d="M14 3H5v18h14V8zM14 3v5h5M8 12h8M8 16h6"/>',
    'share': '<path d="M12 16V3m-4 4 4-4 4 4M5 13v8h14v-8"/>',
    'clients': '<circle cx="9" cy="8" r="3"/><path d="M3 21v-3a6 6 0 0 1 12 0v3M16 5a3 3 0 0 1 0 6m2 3a5 5 0 0 1 3 5v2"/>',
    'check': '<rect x="3" y="3" width="18" height="18" rx="4"/><path d="m7 12 3 3 7-7"/>',
    'device': '<rect x="6" y="2" width="12" height="20" rx="2"/><path d="M10 18h4"/>',
    'activity': '<path d="M3 12h4l3-8 4 16 3-8h4"/>',
    'refresh': '<path d="M20 9a8 8 0 0 0-14-3L3 9m0-6v6h6m-5 6a8 8 0 0 0 14 3l3-3m0 6v-6h-6"/>',
    'shield': '<path d="m12 3 8 3v6c0 5-8 9-8 9s-8-4-8-9V6zM8 12l3 3 5-6"/>',
}


def esc(value):
    return html.escape(str(value), quote=True)


def icon(name):
    return f'<svg class="icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{PATHS[name]}</svg>'


def template(template_name, **values):
    return Template((ROOT / 'templates' / f'{template_name}.html').read_text()).substitute(values)


def inline(text):
    """Small, escaped Markdown subset; content never executes raw HTML."""
    pattern = r'(\[[^\]]+\]\([^\s)]+\)|<https?://[^>]+>|`[^`]+`|\*\*[^*]+\*\*|\*[^*]+\*)'
    output = []
    for part in re.split(pattern, text):
        if part.startswith('[') and (match := re.fullmatch(r'\[([^\]]+)\]\(([^\s)]+)\)', part)):
            label, url = match.groups()
            if not url.startswith(('https://', 'mailto:', '/')):
                raise ValueError(f'Unsupported link: {url}')
            output.append(f'<a href="{esc(url)}">{inline(label)}</a>')
        elif part.startswith('<https') and part.endswith('>'):
            output.append(f'<a href="{esc(part[1:-1])}">{esc(part[1:-1])}</a>')
        elif part.startswith('`') and part.endswith('`'):
            output.append(f'<code>{esc(part[1:-1])}</code>')
        elif part.startswith('**') and part.endswith('**'):
            output.append(f'<strong>{inline(part[2:-2])}</strong>')
        elif part.startswith('*') and part.endswith('*'):
            output.append(f'<em>{inline(part[1:-1])}</em>')
        else:
            output.append(esc(part))
    return ''.join(output)


def markdown(source):
    result, paragraph, items, table_rows = [], [], [], []

    def flush():
        if paragraph:
            result.append('<p>' + inline(' '.join(paragraph)) + '</p>')
            paragraph.clear()
        if items:
            result.append('<ul>' + ''.join(f'<li>{inline(x)}</li>' for x in items) + '</ul>')
            items.clear()
        if table_rows:
            header, *rows = table_rows
            result.append('<div class="table-wrap"><table><thead><tr>' + ''.join(f'<th scope="col">{inline(x)}</th>' for x in header) + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join(f'<td>{inline(x)}</td>' for x in row) + '</tr>' for row in rows) + '</tbody></table></div>')
            table_rows.clear()

    for line in source.splitlines() + ['']:
        line = line.strip()
        if not line:
            flush()
        elif line.startswith('# '):
            flush()  # The layout owns the single h1.
        elif match := re.match(r'^(#{2,3}) (.+)$', line):
            flush()
            level, title = len(match[1]), match[2]
            anchor = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
            result.append(f'<h{level} id="{anchor}">{inline(title)}</h{level}>')
        elif line.startswith('- '):
            if paragraph or table_rows:
                flush()
            items.append(line[2:])
        elif line.startswith('|'):
            if paragraph or items:
                flush()
            cells = [x.strip() for x in line.strip('|').split('|')]
            if not all(re.fullmatch(r':?-+:?', x) for x in cells):
                table_rows.append(cells)
        else:
            if items or table_rows:
                flush()
            paragraph.append(line)
    return '\n'.join(result)


def font(size, bold=False):
    return ImageFont.truetype(str(ROOT / 'assets/fonts' / ('archivo-bold.ttf' if bold else 'archivo-regular.ttf')), size)


def social_card(path, app=None):
    canvas = Image.new('RGB', (1200, 630), '#fbfaf7')
    draw = ImageDraw.Draw(canvas)
    draw.text((70, 55), 'KLM LABS  /  INDEPENDENT APP STUDIO', font=font(21, True), fill='#5e5d55')
    draw.line((70, 109, 1130, 109), fill='#dedcd3', width=2)
    if app:
        app_icon = Image.open(ROOT / app['icon'].lstrip('/')).convert('RGB').resize((180, 180), Image.Resampling.LANCZOS)
        canvas.paste(app_icon, (70, 189))
        size = 66
        while draw.textlength(app['name'], font=font(size, True)) > 800:
            size -= 1
        draw.text((292, 192), app['name'], font=font(size, True), fill='#131310')
        draw.text((294, 284), app['pitch'], font=font(35), fill='#5e5d55')
        draw.text((70, 455), f"{app['category']}  /  Made by {app['developer']}", font=font(26), fill='#131310')
        draw.text((70, 515), ORIGIN + '/' + app['slug'] + '/', font=font(22), fill='#5e5d55')
    else:
        draw.text((65, 169), 'Small apps.', font=font(96, True), fill='#131310')
        draw.text((65, 280), 'Real work.', font=font(96, True), fill='#6e6c63')
        draw.text((70, 515), 'Thoughtful tools for the things you do every day.', font=font(29), fill='#131310')
    canvas.save(ROOT / path.lstrip('/'), optimize=True)


def store_buttons(app):
    buttons = []
    for store, label, asset, alt in [('app_store', 'App Store', 'app-store.svg', 'Download on the App Store'), ('google_play', 'Google Play', 'google-play.svg', 'Get it on Google Play')]:
        data = app['stores'][store]
        if data['live']:
            assert data['url'] and data['url'].startswith('https://'), f'{store}: live requires a URL'
            buttons.append(f'<a class="store-badge {store}" href="{esc(data["url"])}"><img src="/assets/badges/{asset}" alt="{alt}" width="{120 if store == "app_store" else 239}" height="{40 if store == "app_store" else 71}"></a>')
        else:
            buttons.append(f'<div class="store-coming-soon" aria-label="{label}: Coming soon"><span>{label}</span><strong>Coming soon</strong></div>')
    return ''.join(buttons)


def render_page(path, content, title, description, app=None, schema=None):
    footer = ''.join(f'<a href="/{app["slug"]}/{key}/">{label}</a>' for key, label in LABELS.items()) if app else '<a href="/#apps">Our apps</a>'
    values = dict(title=esc(title), description=esc(description), canonical=esc(ORIGIN + path), favicon=app['favicon'] if app else '/assets/favicon.png', icon=app['icon'] if app else '/assets/studio-icon.png', social_image=ORIGIN + (app['social_image'] if app else '/assets/social.png'), social_alt=esc(f'{app["name"]} — {app["pitch"]}' if app else 'KLM Labs — Small apps. Real work.'), content=content, footer_links=footer, structured_data='<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False).replace('<', '\\u003c') + '</script>' if schema else '')
    for kind in ['css', 'js']:
        values[f'{kind}_version'] = hashlib.sha256((ROOT / f'assets/site.{kind}').read_bytes()).hexdigest()[:10]
    output = ROOT / path.lstrip('/') / 'index.html'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text('<!-- Generated by scripts/build.py; edit data, content or templates. -->\n' + template('base', **values))


def main():
    apps = [json.loads(p.read_text()) for p in sorted((ROOT / 'data/apps').glob('*.json'))]
    slugs = [app['slug'] for app in apps]
    assert len(set(slugs)) == len(slugs), 'Duplicate app slug'
    cards, urls = [], ['/']
    arrows = {name: icon(name) for name in ['arrow_left', 'arrow_right', 'arrow_down']}
    for app in apps:
        slug = app['slug']
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug), 'Invalid slug'
        for name in ['icon', 'favicon']:
            assert (ROOT / app[name].lstrip('/')).is_file(), f'Missing {name}'
        assert app['screenshots'], 'At least one real screenshot is required'
        for store in app['stores'].values():
            assert type(store['live']) is bool
        google = app['stores']['google_play']['url']
        apple = app['stores']['app_store']['url']
        assert google is None or google == f'https://play.google.com/store/apps/details?id={app["bundle_id"]}', 'Use the canonical Play URL'
        assert apple is None or re.fullmatch(r'https://apps.apple.com/app/id[0-9]+', apple), 'Use the numeric Apple ID'
        social_card(app['social_image'], app)
        values = {k: esc(v) for k, v in app.items() if isinstance(v, str)}
        shots = []
        for i, shot in enumerate(app['screenshots']):
            src = f'/{slug}/screenshots/{shot["file"]}'
            assert (ROOT / src.lstrip('/')).is_file(), f'Missing screenshot: {src}'
            shots.append(f'<figure class="screenshot-card" role="group" aria-roledescription="slide" aria-label="{i + 1} of {len(app["screenshots"])}"><figcaption><span class="shot-number">{i + 1:02d}</span><h3>{esc(shot["title"])}</h3><p>{esc(shot["caption"])}</p></figcaption><div class="screen-frame"><img src="{src}" alt="{esc(shot["alt"])}" width="{shot["width"]}" height="{shot["height"]}" loading="{ "eager" if i < 2 else "lazy" }" decoding="async"></div></figure>')
        values.update(arrows, store_buttons=store_buttons(app), screenshot_count=len(shots), screenshots=''.join(shots), facts=''.join(f'<div><dt>{esc(x["label"])}</dt><dd>{esc(x["value"])}</dd></div>' for x in app['facts']), about=''.join(f'<p>{esc(x)}</p>' for x in app['about']), features=''.join(f'<div class="feature">{icon(x["icon"])}<h3>{esc(x["title"])}</h3><p>{esc(x["text"])}</p></div>' for x in app['features']), version=esc(app['release']['version']), release_label=esc(app['release']['label']), release_text=esc(app['release']['text']), safety=''.join(f'<div class="safety-item">{icon(x["icon"])}<div><h3>{esc(x["title"])}</h3><p>{esc(x["text"])}</p></div></div>' for x in app['safety']), platforms='Android · iPhone' if app['platforms'] == ['Android', 'iOS'] else esc(' · '.join(app['platforms'])))
        schema = {'@context': 'https://schema.org', '@type': 'SoftwareApplication', 'name': app['name'], 'description': app['description'], 'applicationCategory': app['schema_category'], 'operatingSystem': ', '.join(app['platforms']), 'softwareVersion': app['release']['version'], 'url': ORIGIN + f'/{slug}/', 'image': ORIGIN + app['icon'], 'author': {'@type': 'Organization', 'name': app['developer'], 'url': ORIGIN + '/'}}
        render_page(f'/{slug}/', template('app', **values), f'{app["name"]} — {app["pitch"]} | KLM Labs', app['description'], app, schema)
        urls.append(f'/{slug}/')
        for key, label in LABELS.items():
            links = ''.join(f'<a href="/{slug}/{k}/"{ " aria-current=\"page\"" if k == key else "" }>{v}</a>' for k, v in LABELS.items())
            document = template('document', **{**values, 'page_label': label, 'deck': DECKS[key], 'body': markdown((ROOT / 'content' / slug / f'{key}.md').read_text()), 'document_links': links})
            render_page(f'/{slug}/{key}/', document, f'{app["name"]} — {label} | KLM Labs', f'{app["name"]}: {DECKS[key]}', app)
            urls.append(f'/{slug}/{key}/')
        mini_shots = ''.join(f'<img src="/{slug}/screenshots/{shot["file"]}" alt="" width="{shot["width"]}" height="{shot["height"]}" loading="lazy">' for shot in app['screenshots'][:2])
        cards.append(f'<a class="studio-app-card" href="/{slug}/"><div class="studio-card-copy"><img class="card-app-icon" src="{app["icon"]}" alt="" width="80" height="80"><p class="eyebrow">{esc(app["category"])}</p><h3>{esc(app["name"])}</h3><p class="card-pitch">{esc(app["pitch"])}</p><p>{esc(app["description"])}</p><span class="card-cta">Explore the app {arrows["arrow_right"]}</span><small>{esc(app["availability"])}</small></div><div class="studio-card-screens" aria-hidden="true">{mini_shots}<span>Built for your working day.</span></div></a>')
    social_card('/assets/social.png')
    mark = Image.new('RGB', (180, 180), '#131310')
    ImageDraw.Draw(mark).text((23, 51), 'klm', font=font(72, True), fill='#fbfaf7')
    mark.save(ROOT / 'assets/studio-icon.png', optimize=True)
    mark.resize((48, 48), Image.Resampling.LANCZOS).save(ROOT / 'assets/favicon.png', optimize=True)
    render_page('/', template('studio', **arrows, app_count=f'{len(apps):02d}', app_cards=''.join(cards)), 'KLM Labs — Small apps. Real work.', 'An independent app studio making thoughtful tools for everyday tasks. Explore Invoice Maker and apps from KLM Labs.')
    (ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>{ORIGIN}{url}</loc></url>' for url in urls) + '</urlset>\n')
    source_paths = ['README.md', 'CLAUDE.md', 'docs/', 'scripts/', 'data/', 'content/', 'templates/']
    (ROOT / 'robots.txt').write_text('User-agent: *\nAllow: /\n' + ''.join(f'Disallow: /{path}\n' for path in source_paths) + f'Sitemap: {ORIGIN}/sitemap.xml\n')
    print(f'Built {len(urls)} pages and {len(apps) + 1} social images.')


if __name__ == '__main__':
    main()
