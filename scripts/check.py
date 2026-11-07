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
NATIVE_ROUTES = [f'{slug}/{key}/index.html' for slug in ('construction-calc', 'pdf-esign', 'pdf-scanner', 'desk-clock')
                 for key in ('privacy', 'terms', 'support')] + \
                [f'construction-calc/es/{key}/index.html' for key in ('privacy', 'terms', 'support')] + \
                ['construction-calc/index.html', 'construction-calc/es/index.html', 'pdf-esign/index.html', 'pdf-scanner/index.html', 'desk-clock/index.html']
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


# The only phrases in which the Scanner pages may say "free" outside "free trial" (paywall v2, 2026-11-06).
SCANNER_FREE_PHRASES = [
    'keeping documents in the app are free, with no limit', 'Exporting is free for your first 3 documents',
    'uses one of 3 free exports', 'exporting the same document again is free', 'go out as free exports',
    'exporting one of them again is free', 'uses any free exports you have left', 'uses one of your free exports',
    'Scanning is free, and so are your first 3 exported documents', 'scanning and 3 exported documents are free',
    'uses one of the free exports',
]


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
    # Flip Clock 1.1.0 (CR-001 R7, email-capture design F-1 to F-3): optional sign-in and crash reports are disclosed,
    # and 1.0's "no account" lines do not come back.
    clock = {key: ' '.join(' '.join(docs[ROOT / f'desk-clock/{key}/index.html'].words).split())
             for key in ('privacy', 'terms', 'support')}
    for phrase in ['Signing in with Apple or Google', 'Firebase Authentication', 'Delete my account',
                   'never sent to PostHog or RevenueCat', 'Crash reports, from version 1.1.0', 'Email Address and Name']:
        assert phrase in clock['privacy'], f'desk-clock/privacy: lost sign-in or crash disclosure: {phrase}'
    assert 'Signing in with Apple or Google is optional' in clock['terms'], 'desk-clock/terms: lost the optional sign-in line'
    # Paywall v2 (2026-11-06): the clock is free and Clock Pro is a one-time purchase; 1.1.0 sells no subscription.
    for phrase in ['The clock is free', 'Clock Pro is a one-time purchase', "Version 1.0's Yearly plan includes a 7-day free trial"]:
        assert phrase in clock['terms'], f'desk-clock/terms: lost the free clock and Clock Pro wording: {phrase}'
    assert 'The clock, its three faces, alarms and night mode are free' in clock['support'], 'desk-clock/support: lost the free clock answer'
    for key, text in clock.items():
        assert not re.search(r'every feature[^.]*needs|start a free trial or restore|buy Clock Pro, subscribe', text, re.I), f'desk-clock/{key}: 1.1.0 offered a plan it does not sell'
    assert 'Signing in with Apple or Google is optional' in clock['support'], 'desk-clock/support: lost the optional sign-in answer'
    for key, text in clock.items():
        assert not re.search(r'no account and no sign-up|there is no login|no account of its own|do not collect crash reports',
                             text, re.I), f'desk-clock/{key}: 1.0 no-account or no-crash wording regressed'
    # pdf-scanner's brief bans these words (Store copy) outside the trial wording.
    for page in ('privacy/', 'terms/', 'support/', ''):
        key = page.rstrip('/') or 'hub'
        text = ' '.join(docs[ROOT / f'pdf-scanner/{page}index.html'].words)
        assert not re.search(r'stays? on your (iphone|device)', text, re.I), f'pdf-scanner/{key}: claims it stays on the device (iCloud Backup may copy it)'
        assert not re.search(r'\b(secure|security|encrypted|unlimited|HIPAA|bank-grade)\b|protected by', text, re.I), f'pdf-scanner/{key}: banned word'
        # Paywall v2 (2026-11-06): scanning and 3 exports are free. "free" may say only that, in these exact phrases
        # (as the app's StoreCopyTests pin its store text), and the trial; never sell the app as free.
        for allowed in SCANNER_FREE_PHRASES:
            text = text.replace(allowed, '')
        assert not re.search(r'\bfree\b(?! trial)', text, re.I), f'pdf-scanner/{key}: "free" outside the trial and free-export wording'
    # Scanner 1.1.0 (email-capture design F-1 to F-3, analytics-standard §7 and §8): optional sign-in and crash reports are
    # disclosed, and the earlier "no account" and "no crash reports" lines do not come back.
    scanner = {key: ' '.join(' '.join(docs[ROOT / f'pdf-scanner/{key}/index.html'].words).split())
               for key in ('privacy', 'terms', 'support')}
    for phrase in ['Signing in with Apple or Google', 'Firebase Authentication', 'Delete my account',
                   'never sent to PostHog or RevenueCat', 'Crash reports, from version 1.1.0',
                   'could still include part of it', 'Crash Data', 'nine types of data', 'Email Address and Name',
                   'No usage event ever contains']:
        assert phrase in scanner['privacy'], f'pdf-scanner/privacy: lost sign-in or crash disclosure: {phrase}'
    assert 'Signing in with Apple or Google is optional' in scanner['terms'], 'pdf-scanner/terms: lost the optional sign-in line'
    assert 'signing in with Apple or Google is optional' in scanner['support'], 'pdf-scanner/support: lost the optional sign-in answer'
    # Paywall v2 (2026-11-06): Weekly (3-day trial) or Lifetime, with Yearly (7-day trial) only when Weekly can't load.
    for key in ('terms', 'support'):
        for phrase in ['3-day free trial', '7-day free trial', "instead of Weekly only if the Weekly plan can't be loaded"
                       if key == 'terms' else "If the Weekly plan can't be loaded, the app shows Yearly instead"]:
            assert phrase in scanner[key], f'pdf-scanner/{key}: lost the plan wording: {phrase}'
    for key, text in scanner.items():
        assert not re.search(r'no account and no sign-up|there is no login|no account of its own|do not collect crash reports'
                             r'|never asks for your name|we do not collect your name|six types of data|no event ever contains', text, re.I), \
            f'pdf-scanner/{key}: pre-1.1.0 no-account or no-crash wording regressed'


if __name__ == '__main__':
    main()
