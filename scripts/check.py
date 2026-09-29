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
    for registered in ['index.html', 'invoice-creator/index.html', 'invoice-creator/privacy/index.html', 'invoice-creator/terms/index.html', 'invoice-creator/support/index.html'] + NATIVE_ROUTES:
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
    # Paid launch (2026-09-23): the app sells auto-renewing subscriptions, so the
    # FB-078 free-app wording is now false and the store-required disclosures must stay.
    assert not re.search(r'free to use|sells nothing|no in-app purchases', terms, re.I), 'Free-app wording regressed'
    for phrase in ['renews automatically', '7-day free trial', 'at least 24 hours before', 'Restore purchases',
                   'Deleting the app does not cancel a subscription.', 'reportaproblem.apple.com',
                   'Standard End User Licence Agreement', 'KLM Labs never sees your card or bank details']:
        assert phrase in terms, f'Terms lost subscription disclosure: {phrase}'
    assert 'RevenueCat' in privacy and 'KLM Labs never receives or stores your card or bank details' in privacy, 'Privacy lost RevenueCat disclosure'
    support = ' '.join(docs[ROOT / 'invoice-creator/support/index.html'].words)
    for phrase in ['Restore purchases', 'Cancel Subscription', 'reportaproblem.apple.com']:
        assert phrase in support, f'Support lost subscription help: {phrase}'
    check_native(docs)
    print(f'PASS: {len(paths)} pages, {links} internal references, metadata, FB-066 wording and subscription disclosures.')


# The native iOS apps' legal and support pages: URLs the apps and App Store Connect already point at.
NATIVE_ROUTES = [f'{slug}/{key}/index.html' for slug in ('construction-calc', 'pdf-esign', 'pdf-scanner')
                 for key in ('privacy', 'terms', 'support')] + \
                [f'construction-calc/es/{key}/index.html' for key in ('privacy', 'terms', 'support')] + \
                ['construction-calc/index.html', 'construction-calc/es/index.html', 'pdf-esign/index.html', 'pdf-scanner/index.html']
EULA = 'https://www.apple.com/legal/internet-services/itunes/dev/stdeula/'
NATIVE_DISCLOSURES = {
    'en': {'terms': ['renews automatically', '7-day free trial', 'at least 24 hours before', 'Restore',
                     'Deleting the app does not cancel a subscription.', 'reportaproblem.apple.com', 'Standard EULA'],
           'privacy': ['PostHog', 'RevenueCat', 'KLM Labs never receives or stores your card or bank details',
                       'IP address', 'never reads your device\'s GPS'],
           'support': ['Cancel Subscription', 'Restore', 'reportaproblem.apple.com']},
    'es': {'terms': ['se renueva automáticamente', '7 días de prueba gratis', 'al menos 24 horas antes', 'Restaurar',
                     'Eliminar la app no cancela una suscripción.', 'reportaproblem.apple.com', 'EULA estándar'],
           'privacy': ['PostHog', 'RevenueCat', 'KLM Labs nunca recibe ni guarda los datos de tu tarjeta ni de tu banco',
                       'dirección IP', 'nunca lee el GPS de tu dispositivo'],
           'support': ['Cancelar suscripción', 'Restaurar', 'reportaproblem.apple.com']},
}


def check_native(docs):
    for route in NATIVE_ROUTES:
        parts = route.split('/')
        if len(parts) < 3 or parts[-2] not in ('privacy', 'terms', 'support'):
            continue
        lang, key = ('es' if parts[1] == 'es' else 'en'), parts[-2]
        doc = docs[ROOT / route]
        text = ' '.join(' '.join(doc.words).split())
        for phrase in NATIVE_DISCLOSURES[lang][key]:
            assert phrase in text, f'{route}: lost disclosure: {phrase}'
        if key == 'terms':
            assert EULA in doc.refs, f'{route}: lost the Standard EULA link'
        assert 'mailto:klm.labs.inc@gmail.com' in doc.refs, f'{route}: lost the support address'
        assert 'klmlabs.com' not in text, f'{route}: names klmlabs.com, a domain KLM Labs does not own'
        html = (ROOT / route).read_text()
        assert f'<html lang="{"es-MX" if lang == "es" else "en"}"' in html, f'{route}: wrong html lang'
    # pdf-scanner's brief bans these words (Store copy) outside the trial wording.
    for page in ('privacy/', 'terms/', 'support/', ''):
        key = page.rstrip('/') or 'hub'
        text = ' '.join(docs[ROOT / f'pdf-scanner/{page}index.html'].words)
        assert not re.search(r'stays? on your (iphone|device)', text, re.I), f'pdf-scanner/{key}: claims it stays on the device (iCloud Backup may copy it)'
        assert not re.search(r'\b(secure|security|encrypted|unlimited|HIPAA|bank-grade)\b|protected by', text, re.I), f'pdf-scanner/{key}: banned word'
        assert not re.search(r'\bfree\b(?! trial)', text, re.I), f'pdf-scanner/{key}: "free" outside the trial wording'


if __name__ == '__main__':
    main()
