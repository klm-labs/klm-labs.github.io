# FB-066 publication review — 2026-09-11

Reviewed app source at `/work/apps/invoice-creator`, commit
`b8fcde72fa04491b2283b44ae18756167f56261d`. This task only reads that repository.
Source files were reviewed directly; no app code, installation or checkout was changed.

## Behavior verified

- `lib/analytics.ts`: `analyticsAvailable()` is native platform plus a nonempty
  bundled key. `analyticsEnabled()` returns that capability, without reading a
  user setting. `initAnalytics()` uses `defaultOptIn: true` and calls `optIn()`
  to clear persisted SDK state from older versions before capturing/flushing.
- `lib/__tests__/analytics.test.ts`: tests pin all legacy preference states,
  SDK reactivation, iOS/Android behavior, web/key-free inactivity, all three
  replay masks, console capture off and geolocation remaining enabled.
- The key-free/web guard prevents SDK construction, capture and flushing.
  Keyed native builds collect restricted events, app/build/platform/environment,
  random device/session identifiers, IP-derived coarse location and masked replay.
- `app.config.ts`: Expo Updates URL is configured and runtime uses `fingerprint`;
  no `enabled: false` or launch-check override. Native release builds check at
  launch, independently of PostHog. Installed Expo Updates request code in
  `node_modules/expo-updates/.../FileDownloader` confirms `EAS-Client-ID`.
  [Expo’s documentation](https://docs.expo.dev/eas-update/how-it-works/) explains
  launch update behavior. Web and development execution differ from native release.
- `docs/store/play-data-safety-answers.md` and `apple-privacy-answers.md` agree
  that keyed-native collection is required. Both include update identifiers and
  metadata even without PostHog. Apple conservatively declares device linkage.
- `app.config.ts` derives `com.klmlabs.invoicecreator`; `store.config.json`
  confirms that same Android package and Apple bundle identifier.

## Published policy correction

Old published HTML: analytics was optional via **Settings → Analytics**; saved
preferences controlled collection, and invalid/unreadable preferences left it off.

New published policy: **Collection is always enabled in native builds with a
bundled analytics key. The app provides no analytics setting. Builds without a
key and the web build send no PostHog data. Update checks operate independently
of analytics.** Updating/uninstalling does not delete processor-held records.

The app’s 2026-09-09 Markdown draft already describes that core behavior correctly.
The website now publishes it with the following explicit corrections. These
should be reconciled into the read-only app repo by its owning session.

| App Markdown claim | Site text / reason |
| --- | --- |
| Draft revision, publication pending | Effective 2026-09-11; URL/contact links are supplied by the shared layout. |
| Mentions removal of opt-out and a stored preference | Same behavior in direct language: automatic keyed-native collection, no analytics setting; no obsolete control terminology. |
| “An anonymous identifier” | “A pseudonymous identifier”; explains linkage to the same device. Random IDs do not establish unlinked data; this matches the Apple declaration. |
| PostHog always in the US and no own-purpose processing | US is the code’s default endpoint, overridable per build. Links PostHog’s privacy policy without asserting an unverified contractual configuration. |
| Replay kept for 30 days then automatically deleted | Uses processor retention settings and offers retention/deletion inquiries. The repository does not prove the project’s actual setting. [PostHog retention](https://posthog.com/docs/session-replay/recording-retention) is configurable by project/plan and expiration is not immediate deletion. |
| Each app open checks Expo, without build qualification | Qualifies this as native release launch checks, independent of PostHog, including key-free release builds. Web/development execution differs. |
| Expo installation ID “does not identify you” | It is not an account or hardware identifier, but links requests to the same installation. |
| Reinstall always generates a new Expo identifier | Removes the categorical reinstall guarantee; explicitly says removing the app does not delete Expo’s retained records. Backup/restore behavior is outside the app module. |
| Dates/platform will locate analytics and deletion will be confirmed | Dates/platform help investigation; more information may be needed, and the team explains which pseudonymous records can be found/deleted. An operational deletion guarantee is not established by code. |
| “We will honour” all listed rights | Respond in accordance with applicable law, retaining contact, access and deletion routes. |

Otherwise the policy retains the local-data, restricted-events, coarse-location,
all-text/image/picker masking, photo-library, PDF-sharing, children’s-data and rights
sections. No analytics-control wording appears in the generated policy. The terms
body (including its existing purchase/licensing provisions) is preserved exactly,
apart from whitespace and markup; it contains no analytics opt-out claim.
Support now distinguishes offline invoicing/local deletion from network collection
and records held by service providers.

## Store facts and follow-up for the app owner

- Canonical Play URL returned **404**, expected during closed testing:
  https://play.google.com/store/apps/details?id=com.klmlabs.invoicecreator.
  This remains a live link by explicit founder direction; the page says it is in
  closed testing. No URL change is needed for production.
- `https://itunes.apple.com/lookup?bundleId=com.klmlabs.invoicecreator` returned
  HTTP 200, `resultCount: 0`. No `ascAppId`, numeric App Store URL or Apple ID was
  found in store config, EAS config or store documentation. App Store is a
  non-interactive “Coming soon” state; see README line-edit instructions for launch.
- `store/android/metadata.json` still claims “no analytics”; iOS `description`
  also says there are no analytics. Those statements are false for keyed native
  builds and were **not reused** on the website. App owner: remove those claims
  in both source metadata files and reconcile actual store-console text.
- App owner: copy the site’s reviewed privacy corrections into
  `docs/store/privacy-policy.md`, mark the draft published, and reconcile the
  console declarations against the actual submitted binary. Verify the release
  analytics host, masking, retention and operational deletion handling. These
  console/processor states cannot be established from the site repository.
- Terms retain their original purchase wording at the user’s direction. No claim
  about prices, subscriptions or an assigned content rating was added to the listing.

## Real screenshots used

All sources are under the app repo; all destinations are in the site repo.
Each entire capture is resized to 576 × 1280 and encoded as WebP quality 86.

| Source | Destination |
| --- | --- |
| `docs/design/walkthrough/android-2026-09-10-AriWHd/19-home-with-invoice.png` | `invoice-creator/screenshots/01-invoices.webp` |
| `docs/design/walkthrough/android-2026-09-10-AriWHd/13-invoice-editor.png` | `invoice-creator/screenshots/02-create-invoice.webp` |
| `docs/design/walkthrough/android-2026-09-10-AriWHd/22-client-editor-history.png` | `invoice-creator/screenshots/03-client-history.webp` |
| `docs/design/walkthrough/android-2026-09-10-AriWHd/25-settings-defaults.png` | `invoice-creator/screenshots/04-invoice-defaults.webp` |
| `docs/design/walkthrough/android-2026-09-10-AriWHd/23-settings.png` | `invoice-creator/screenshots/05-settings.webp` |

Both September 10 capture folders were visually compared. This set contains no
keyboard, error page, Preview screen or junk test names. The current captures
retain the app’s existing presentation; replace them after round-4 fixes using
the documented file-replacement/data-list workflow.

## Verification evidence

- Local checks passed for all five pages and 109 internal references.
- Ten browser renders at 390 × 844 and 1440 × 900: no page overflow, missing
  images, console errors or external runtime resources; WCAG A/AA axe checks
  reported zero violations at both widths. Keyboard/reduced-motion carousel
  navigation and content without JavaScript also passed.
- A second-app fixture outside this repository built nine pages from data,
  content and assets alone. Both unavailable stores rendered without links;
  a live store without a URL failed validation.
- Rebuilding twice produced byte-identical HTML, social PNGs and sitemap.
- Terms body compared equal to the previous published source after whitespace
  normalization. The privacy-control regression check passed.
- Source-file hashes below record the read-only behavior review.

```text
088847234566e5789305a807fa5193a45d4349e43a1d906608154b2a9eba1cbd  docs/store/privacy-policy.md
667ce2f10b587aba96af39177261ca5c2f3dd3b06216c52a3a01bb675ac67f3d  lib/analytics.ts
7b942f4f3aef22401cae57ead9204377790b1fbce01db617626268bcc853acc2  lib/__tests__/analytics.test.ts
c4a57a950c9cbe39390998ec07c8cc5e392b2b2bbe8c9165f3fda24f58b274e3  app.config.ts
7120b197ccb4d9bd6060eb24e739dc8f3a1791c4b59d6b7a0c30d038b2351aa5  docs/store/play-data-safety-answers.md
f39d73828262f0a76700e8fb403b4305a760cc47a81d58568531af4d4ea28aea  docs/store/apple-privacy-answers.md
```
