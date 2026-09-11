# Asset provenance

All public assets are served from this repository. The browser makes no external
font, badge, script, analytics or image request.

- **App icon:** `invoice-creator/{icon,favicon}.png`, resized from the app repo’s
  `assets/icon.png`; no artwork edits. The small original vermilion mark remains
  part of that icon. The website’s action and focus colors are near-black ink.
- **Screenshots:** source paths are recorded per entry in
  `data/apps/invoice-creator.json` and `docs/fb-066-review.md`. Whole real Android
  captures, resized and compressed to WebP. Presentation frames live in CSS.
- **Archivo:** regular, semibold and bold, from the app’s installed
  `@expo-google-fonts/archivo`; license in `fonts/Archivo-OFL.txt`.
- **IBM Plex Mono:** regular, from `@expo-google-fonts/ibm-plex-mono`; license in
  `fonts/IBMPlexMono-OFL.txt`. WOFF2 files contain the Latin/extended-Latin and
  punctuation subset used by this English site. The two Archivo TTFs generate
  social images at build time and are not requested by browsers.
- **KLM studio mark and social images:** generated typography from committed
  fonts by `scripts/build.py`. App social cards use the app’s actual icon.
- **Interface icons:** simple inline SVG paths defined once by the generator.

## Official store badges

Downloaded unchanged on 2026-09-11:

| Local asset | Official source |
| --- | --- |
| `badges/google-play.svg` | Google Partner Marketing Hub’s “Google Play Badge guidelines.zip” → `Get it on Google Play Badges/Digital/svg/GetItOnGooglePlay_Badge_Web_color_English.svg` |
| `badges/app-store.svg` | https://developer.apple.com/assets/elements/badges/download-on-the-app-store.svg |

Follow [Apple’s marketing guidelines](https://developer.apple.com/app-store/marketing/guidelines/)
and [Google Play’s badge guidelines](https://partnermarketinghub.withgoogle.com/brands/google-play/google-play/lockups-icons-badges/?folder=65714).
Do not recolor, distort, rewrite, or recreate the artwork. Apple’s badge has a
minimum onscreen height of 40 px and quarter-height clear space. Google’s badge
must be at least as large as accompanying store badges and have quarter-height
clear space. CSS preserves both aspect ratios, 13 px vertical clear space and a
26 px gap between badges (at least one-quarter of each badge’s height on each
side). Apple’s live badge renders first at 48 px high. Google’s current SVG is
about 48.6 px high, at least as large as Apple’s. Both retain their minimum
40 px height on the narrowest screens, with a 22 px gap; page gutters supply outer clear space.
Trademark credit is in the footer. The download link in the official hub is a
temporary signed URL, so only the original artwork is committed, not that URL.

The App Store download artwork is retained for launch but is not displayed while
the app is unavailable. Its current “Coming soon” state is plain text, not a
modified badge and not a link. Google’s canonical link remains active during
closed testing by the founder’s explicit direction, with the availability note.
