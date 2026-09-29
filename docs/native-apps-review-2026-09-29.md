# Native iOS apps: policy review, 2026-09-29

The first publication of the Terms, Privacy and Support pages for three native iOS apps. Their builds and App
Store Connect records already linked to these URLs, which returned 404. Each app repository was only read, on
branch `build/v1` with `git show`; nothing there was changed.

| App | Repository and commit | App Store Connect App Privacy |
| --- | --- | --- |
| Fraction Feet Inch Calculator (`construction-calc`) | `klm-labs/construction-calc` `7bb50e5eed7685f0b7f1932036b2a29ad64b9f98` | Published. As read back on 2026-09-28 21:55Z (`docs/build/app-privacy.md`): Product Interaction, Other Usage Data and Coarse Location for Analytics; Purchase History for App Functionality and Analytics; all Not Linked to You; no tracking; no Identifiers |
| Signer: Sign PDF Documents (`pdf-esign`) | `klm-labs/pdf-esign` `97a7c310953cc6e481eee8a9c9bb37543e60ed66` | Not entered yet (`docs/build/launch-checklist.md`) |
| PDF Scanner App: OCR & Search (`pdf-scanner`) | `klm-labs/pdf-scanner` `b09dfca921d8409ad07b71cf07391faf1a6a047f` | No App Store Connect record yet. Its analytics, purchases and reminder code isn't written yet |

The live App Privacy page could not be read again on 2026-09-29. The saved App Store Connect web session had
expired, and signing in again needs the account holder's password and two-factor code. The construction-calc
answers above are the ones its repository recorded from App Store Connect on 2026-09-28.

## What the pages rely on

- **Analytics.** In construction-calc and pdf-esign, `posthog-ios` 3.85.0 is set up with person profiles,
  autocapture, screen views, session replay, surveys and feature flags all off. The properties the apps add
  are limited:
  - pdf-esign: fixed enums only.
  - construction-calc: short app-defined strings, which include the RevenueCat offering id.
  - pdf-scanner: its planned wrapper allows counts, enums and booleans only.

  The SDK adds its own properties:
  - app name, version, build and namespace (the bundle id);
  - device maker, model and type, and `$device_name`, which on iOS is `UIDevice.model` (for example "iPhone");
  - OS name and version, screen size, locale and time zone;
  - Wi-Fi or cellular, and whether the app is a simulator, TestFlight or sideloaded build;
  - the library and its version;
  - a random distinct ID and a session ID.

  It reads no advertising identifier. The host is `us.i.posthog.com`, shared project 572434. That project
  keeps the client IP, so PostHog derives a country and city from it, and every policy says so. pdf-scanner's
  pages describe the same setup as planned behavior; they must be rechecked against its code once written.
- **Purchases.** RevenueCat runs with no app user ID of its own (anonymous) and gets
  `trackCustomPaywallImpression` and `attribution.setPostHogUserID`. construction-calc has the RevenueCat →
  PostHog integration on. For pdf-esign it's unknown, so its policy says "may send". For pdf-scanner the link
  is conditional (Gate 2 D14), so its policy says "may".
- **Plans.** Each policy's plans come from that repository's `docs/store/iap-spec.json` and its Gate 2
  decisions:
  - construction-calc: Yearly US$9.99 with a 7-day trial; Lifetime US$19.99 with Family Sharing.
  - pdf-esign: Yearly US$19.99 with a 7-day trial; Lifetime US$39.99; no Family Sharing.
  - pdf-scanner: the same prices as pdf-esign; no Family Sharing.
  - construction-calc and pdf-esign have the 16-day billing grace period and a local trial reminder 2 days
    before the end.
  - For pdf-scanner, Gate 2 (D13, D15) specifies both. Production grace is turned on only after the sandbox check
    is recorded.
- **Support address.** `klm.labs.inc@gmail.com`, the address construction-calc's app already uses.

## Differences for the app teams

1. **construction-calc.** `Sources/PrivacyInfo.xcprivacy` lists Purchase History for App Functionality only.
   App Store Connect lists App Functionality and Analytics. The code links purchases to analytics through
   `setPostHogUserID` and the RevenueCat → PostHog integration, so App Store Connect is the accurate one. Add
   Analytics to the manifest's Purchase History purposes.
2. **pdf-esign: App Privacy not entered.** The planned answers in `docs/build/app-privacy.md` (Product
   Interaction; Purchase History for App Functionality) leave out three things:
   - Coarse Location, since PostHog stores the IP in the shared project.
   - Other Usage Data, which the PostHog SDK manifest declares and the doc treats only as a flag.
   - Analytics as a Purchase History purpose. Signer already sends `purchase` events with the plan type straight
     to PostHog (`PaywallModel.swift`). If the RevenueCat → PostHog integration is on, it also sends renewals and
     cancellations.

   construction-calc's published answers are the model. The doc's event table also lists 7 events. The code
   sends 11, adding `paywall_closed`, `purchase_cancelled`, `purchase_failed` and `restore`.
3. **pdf-esign support address.** `Sources/Screens/SupportMail.swift` sends Settings → Contact Support to
   `support@klmlabs.com`. KLM Labs does not own that domain: it has been registered to someone else since
   2000, and it uses Outlook mail servers. Change it to `klm.labs.inc@gmail.com`, the address the published
   pages give.
4. **pdf-scanner.** The brief expects Identifiers → User ID in its App Privacy answers, unlike the other two
   apps. construction-calc's `docs/build/app-privacy.md` argues that the random, app-scoped PostHog and
   RevenueCat IDs are not Identifiers. Pick one answer for all three apps. The pdf-scanner pages follow its
   locked brief and Gate 2 decisions, so recheck them against the code in build part P4. Its brief's banned
   words, and the rule against claiming documents "stay on your iPhone", are enforced by `check.py`.
5. **Retention.** The policies give a rule, not a period: records are kept as long as needed to run, support and
   improve the app, or as the law requires. Set the PostHog project's data retention, and decide how long
   RevenueCat and support mail are kept. Then replace the rule with real periods.

## Cross-model review

Codex (read-only `codex exec`, 2026-09-29) reviewed the pages against the code and this evidence. It made 15
findings.

- **Accepted and fixed:**
  - the Signer access rules after Pro ends, and its password import;
  - the missing SDK properties;
  - the processor-protection statement (Guideline 5.1.1(i));
  - the email-correspondence section;
  - the history sharing and backup caveats;
  - the calculator's 1,000-entry history cap and its More (…) → Clear All path;
  - the conditions for the reminder page;
  - the event-property wording;
  - "anonymous" replaced by "a random identifier";
  - this file's three overstatements.
- **Modified:**
  - Retention: Codex asked for concrete periods, which are not set. The pages state the rule instead, and item 5
    above tracks the real periods.
  - Device name: `$device_name` is described as the generic model name, not the user's device name, as Codex
    assumed.
