#!/usr/bin/env python3
"""Check the committed output, registered routes, metadata and privacy regression."""
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent.parent


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.refs, self.ids, self.h1, self.canonical, self.social, self.words = [], set(), 0, [], [], []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f'Duplicate id: {attrs["id"]}'
            self.ids.add(attrs['id'])
        if tag == 'h1':
            self.h1 += 1
        if tag == 'img':
            assert 'alt' in attrs, 'Image missing alt'
        for attr in ('href', 'src'):
            if attr in attrs:
                self.refs.append(attrs[attr])
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical.append(attrs['href'])
        if tag == 'meta' and attrs.get('property') == 'og:image':
            self.social.append(attrs['content'])

    def handle_data(self, data):
        self.words.append(data)


def main():
    paths = [ROOT / 'index.html'] + sorted(p for folder in (ROOT / 'data/apps').glob('*.json') for p in (ROOT / json.loads(folder.read_text())['slug']).rglob('index.html'))
    docs = {p: Document(p.read_text()) for p in paths}
    assert len(paths) >= 5
    for registered in ['index.html', 'invoice-creator/index.html', 'invoice-creator/privacy/index.html', 'invoice-creator/terms/index.html', 'invoice-creator/support/index.html']:
        assert ROOT / registered in docs, f'Registered route lost: {registered}'
    links = 0
    for path, doc in docs.items():
        assert doc.h1 == 1, f'{path}: expected one h1'
        route = '/' + str(path.parent.relative_to(ROOT)).strip('.')
        if route != '/':
            route += '/'
        assert doc.canonical == ['https://klm-labs.github.io' + route]
        assert len(doc.social) == 1
        assert (ROOT / urlparse(doc.social[0]).path.lstrip('/')).is_file()
        for ref in doc.refs:
            parsed = urlparse(ref)
            if parsed.scheme in ('mailto', 'https', 'http'):
                continue
            target = ROOT / unquote(parsed.path).lstrip('/') if parsed.path.startswith('/') else path.parent / unquote(parsed.path)
            if target.is_dir():
                target /= 'index.html'
            assert target.is_file(), f'{path}: broken link {ref}'
            if parsed.fragment and target in docs:
                assert parsed.fragment in docs[target].ids, f'{path}: missing anchor {ref}'
            links += 1
    privacy = ' '.join(docs[ROOT / 'invoice-creator/privacy/index.html'].words)
    assert not re.search(r'opt[ -]out|turn off|disable|choose whether|preference', privacy, re.I), 'Analytics-control wording regressed'
    assert 'Collection is always enabled in native builds with a bundled analytics key.' in privacy
    assert 'Builds without a key and the web build send no PostHog data.' in privacy
    assert 'Update checks operate independently of analytics.' in privacy
    terms = ' '.join(docs[ROOT / 'invoice-creator/terms/index.html'].words)
    assert not re.search(r'opt[ -]out', terms, re.I)
    assert 'Invoice Creator is free to use and sells nothing inside the app.' in terms
    assert not re.search(r'Some features require a purchase|subscription renews|free trial|Restore purchases', terms, re.I), 'FB-078 purchase wording regressed'
    print(f'PASS: {len(paths)} pages, {links} internal references, metadata and FB-066/FB-078 wording.')


if __name__ == '__main__':
    main()
