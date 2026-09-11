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

## 2026-09-11 — independent-check follow-up

The earlier notes describe publication `0306cf1`. This section supersedes the
purchase-preservation note and expands the technical-data inventory. App source
was rechecked at `b8fcde72fa04491b2283b44ae18756167f56261d`, without edits.
Installed versions: `posthog-react-native` 4.63.5, `@posthog/core` 1.48.8,
`expo-updates` 57.0.16, and `expo-file-system` 57.0.5. All app paths below are
relative to `/work/apps/invoice-creator`. SDK citations refer to installed files,
not a different release's documentation. The two React Native SDK files are
minified onto line 1; function names below identify the relevant code on that line.

### FB-078: free app

Replaced only the purchases/renewals/trials/restoration/refunds section with:
“Invoice Creator is free to use and sells nothing inside the app. If paid features
are added in the future, these terms will be updated before those features launch.”
The effective date is now 2026-09-11, with a one-line change note. All other terms
text is preserved. The advance-update commitment is the publisher's instruction.

Evidence: `docs/product-spec.md:354–358` specifies free v1 with no paywall;
`package.json:7–68` contains no billing library. Enumerating all production routes
under `app/` found no purchase screen. Searching those routes for purchase,
paywall, billing, RevenueCat, restoration and subscription calls found only the
unrelated AppState listener named `subscription` at `app/_layout.tsx:195–200`.
Unused purchase/paywall event names in `lib/analytics.ts:84–89` do not implement
purchases or prove that those events are emitted.

2026-09-11 — FB-078 remnant follow-up: removed the nonexistent purchase/licensing-check phrase and already-bought paid-feature sentence from Invoice Creator's terms, extended the change note, and retained the effective date and liability cap. The terms prose is app-specific Markdown; only the document layout is shared. The listing, app data, privacy, support, studio page and generated HTML contain no other false purchase claims; invoice prices/payment statuses, conditional future paid features, licences and statutory remedies remain accurate.

### FB-066: automatic analytics fields

The policy's plain-language list now covers the following complete automatic
event inventory for this app configuration, including its existing identifier
paragraph. Conditional feature fields are explicitly qualified.

| Policy claim / actual fields | Installed code evidence |
| --- | --- |
| App version, build number, build environment, platform: `app_version`, `build_number`, `environment`, `platform` | `lib/analytics.ts:120–128`, registered at `:196`. These are app-supplied super properties. |
| Device category: `$device_type`, reported as `Mobile` on these native platforms | `node_modules/posthog-react-native/dist/native-deps.js:1`, `getDeviceType` and `getAppProperties`. |
| Screen width and height: `$screen_width`, `$screen_height` | `node_modules/posthog-react-native/dist/posthog-rn.js:1`, `getCommonEventProperties`, reads React Native `Dimensions.get('screen')`. |
| Analytics library name/version: `$lib`, `$lib_version` | `node_modules/@posthog/core/dist/posthog-core-stateless.js:211–215`; React Native `getLibraryId`/`getLibraryVersion` in `dist/posthog-rn.js:1`. |
| Event time and random event ID: envelope `timestamp`, `uuid` | `node_modules/@posthog/core/dist/posthog-core-stateless.js:662–667`, `prepareMessage`. |
| Random device/activity identity and session ID: envelope `distinct_id`, property `$session_id` | `node_modules/@posthog/core/dist/posthog-core.js:127–173`; event envelope in `posthog-core-stateless.js:249–260`. |
| No identified login/person-profile processing: `$is_identified`, `$process_person_profile` | `node_modules/@posthog/core/dist/posthog-core.js:228–237`, `:813–832`; default `identified_only` at `:46`. App construction/capture at `lib/analytics.ts:155–196,209–215`; no app calls to identify, group, create a person profile, or set person properties. |
| Available feature-configuration names/values and active list: `$feature/<name>`, `$active_feature_flags` | `node_modules/@posthog/core/dist/posthog-core.js:117–125,660–661`. Remote flag loading is allowed by the default at `:44` and initialization at `:422`; this does not imply the app has a feature-configuration screen. |

Optional dependencies were checked with `require.resolve` from the installed
PostHog package, not just the app's direct-dependency list. Each SDK optional
loader catches missing-module errors (`dist/optional/Optional*.js:1`).

| Optional module | Installed / consequence in this app |
| --- | --- |
| `expo-device` | Absent. No manufacturer, model, OS name/version or emulator flag from it. |
| `react-native-device-info` | Absent. No fallback for device details or app identity. |
| `expo-application` | Absent. No SDK `$app_name`, `$app_namespace`, `$app_version` or `$app_build`; the separate app-version/build super properties above are still sent. |
| `expo-localization` | Absent. No device locale or timezone from it. |
| `react-native-localize` | Absent. No fallback for device locale or timezone. |
| `expo-file-system` and its `legacy` export | Present. Used for local queue/identifier persistence; do not add event properties. |
| `@react-native-async-storage/async-storage` | Absent. The filesystem supplies persistence instead. |

All property branches and storage fallbacks are in
`node_modules/posthog-react-native/dist/native-deps.js:1`, `getAppProperties` and
`buildOptimisticAsyncStorage`. App config supplies no custom property override
(`lib/analytics.ts:155–191`). Absent-module properties have not been added to the
policy. Device locale/timezone absence does not remove server-derived location.

### FB-066: Expo request headers

In this table, **Android downloader** means
`node_modules/expo-updates/android/src/main/java/expo/modules/updates/loader/FileDownloader.kt`;
**iOS downloader** means
`node_modules/expo-updates/ios/EXUpdates/AppLoader/FileDownloader.swift`.

| Policy claim / actual headers | Installed code evidence |
| --- | --- |
| Platform, runtime fingerprint and build channel: `Expo-Platform`, `Expo-Runtime-Version`, `expo-channel-name` | Android downloader `:894–905,919–922`; iOS downloader `:454–461,470–471`; `app.config.ts:49–50`; configured release channels in `eas.json:22,34`. |
| Random installation ID: `EAS-Client-ID` | Android downloader `:900`; iOS downloader `:459`. Generation/persistence: `node_modules/expo-eas-client/android/src/main/java/expo/modules/easclient/EASClientID.kt:20–30` and `node_modules/expo-eas-client/ios/EASClient/EASClientID.swift:9–12,25–32`. No hardware/account value enters generation. |
| Current and embedded update IDs, when available: `Expo-Current-Update-ID`, `Expo-Embedded-Update-ID` | Android downloader `:946–951`; iOS downloader `:365–371`. These identify software updates, not individual people. |
| Protocol/API versions (`1`), native environment (`BARE`), accepted formats and JSON errors: `Expo-Protocol-Version`, `Expo-API-Version`, `Expo-Updates-Environment`, `Accept`, `Expo-JSON-Error` | Android downloader `:894–899`; iOS downloader `:454–460`. |
| Recent failed update IDs and saved fatal-error details, conditional: `Expo-Recent-Failed-Update-IDs`, `Expo-Fatal-Error` | Android downloader `:908–916,953–959`; iOS downloader `:373–379,463–467`. Both truncate fatal-error headers to 1,024 characters. Android serializes the exception in `launcher/NoDatabaseLauncher.kt:32–36`; iOS serializes fatal app errors/exceptions in `node_modules/expo-updates/ios/EXUpdates/ErrorRecovery.swift:370–384`. |
| Server-provided headers echoed on later checks, when present | Android downloader `:939–940`; iOS downloader `:347–350`. |
| Download requests also identify the requested update and can request patches: `Expo-Requested-Update-ID`, `A-IM: bsdiff` | Android downloader `:770–805,965–982`; iOS downloader `:137–143,391–409,537–545` (`headersForPatch`). |

`Expo-Extra-Params` is conditional on stored client parameters (Android downloader
`:942–944`, iOS `:354–360`); no production app code calls `setExtraParamAsync`, so
no custom parameters are claimed. `expo-expect-signature` requires a configured
signing certificate (Android `:925–926`, iOS `:474–475`); this app has none in
`app.config.ts:49–50`. The policy does not claim these optional headers are sent.
Request headers are separate from generic HTTP transport headers supplied by the
operating system. No app invoice/client fields are added to the update request.

### FB-066: verified IP storage

On 2026-09-11, a read-only `GET /api/projects/{id}/` returned HTTP 200 with
**`anonymize_ips: false`**. The project was matched to the app's configured
analytics key by an in-memory equality check. Credentials and the unfiltered
response were neither printed nor saved; no PostHog setting was changed.

Published sentence: **“PostHog stores your IP address with analytics events.”**
The existing approximate-location explanation is retained. PostHog's
[IP capture documentation](https://posthog.com/docs/privacy/data-collection#ip-data-capture)
describes the project setting. The
[setting's implementation, line 12](https://github.com/PostHog/posthog/blob/e82b17403425a1533b5be614f50a289ecc736b4c/frontend/src/scenes/settings/environment/IPCapture.tsx#L12)
maps `anonymize_ips` to discarding client IP data; the
[ingestion step, lines 41–43](https://github.com/PostHog/posthog/blob/e82b17403425a1533b5be614f50a289ecc736b4c/nodejs/src/ingestion/common/steps/event-processing/prepare-event-step.ts#L41)
removes `$ip` only when that flag is true. The app does not override the SDK's
GeoIP-enabled default (`node_modules/@posthog/core/dist/posthog-core.js:36–40`;
`lib/analytics.ts:155–191`). Because discarding is false, no claim about the order
of location derivation versus IP discarding is needed or made.

### Publication corrections and app-owner reconciliation

Privacy remains effective 2026-09-11; its revision note now includes automatic
metadata, IP storage and update headers. The new bullets/sentence above are the
exact additions to reconcile into the app's `docs/store/privacy-policy.md`, which
currently matches the earlier site revision. The Play/Apple declaration drafts
still omit this expanded technical inventory and mark console reconciliation
pending; this site task does not establish that store consoles were updated.

Source files were never loaded at runtime: before changing `robots.txt`, all five
routes at both target sizes requested only route HTML, `assets/` files and app
icons/screenshots. The generator now disallows the seven requested source paths
without changing Pages or `.nojekyll`. Browser checks enforce this separation.

Browser tooling now requires `PLAYWRIGHT_PATH`, `CHROME_PATH` and `RENDER_DIR`,
with explicit missing/invalid-path errors and documented usage. The README's
session URL is removed. Text previously measured at 8–11 px now has a 12 px
minimum, and mobile body copy has a 16 px minimum, including policy tables/code,
availability copy, feature descriptions and screenshot captions. Checks inspect
rendered text-node computed styles rather than inferring sizes from CSS.

Follow-up validation passed: five generated pages and 109 internal references;
all ten final renders at 390 × 844 and 1440 × 900 had HTTP 200, no console errors,
failed requests, broken images, source-directory requests or horizontal overflow.
Minimum computed text size was 12 px on every page, with mobile body copy at
least 16 px. All pages were visually inspected at both sizes. A further font
sweep covered 16 widths from 280 to 2560 px, including each responsive breakpoint;
resource navigation also fits at 280 px. Missing/invalid values for all three
required renderer variables produced clear errors. A second build was byte
identical; the remaining terms compared exactly equal after excluding the
authorized changes. All six privacy-control phrase checks returned zero hits.

Installed SDK file SHA-256 values:

```text
621431506b4890a09b0de9f6cf7768f5a1adb8ab13a274cb07bbff8620700957  node_modules/posthog-react-native/dist/native-deps.js
293ea36cf8acae3134de15d418b8e55160131cb56a455c35a8c1eb9c0f0ceda4  node_modules/posthog-react-native/dist/posthog-rn.js
da122d1efe52189daab98b3df97861600928c0651e92fdc9b495167290208bd7  node_modules/@posthog/core/dist/posthog-core.js
65e97540bad48206dcd7c033090a52802c8dd8888c1fa83d2ac33565af2d2cbf  node_modules/@posthog/core/dist/posthog-core-stateless.js
```
