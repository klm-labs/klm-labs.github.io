# eSign: Document Signer & Fill Privacy Policy

**Effective date:** 2026-11-03

**Contact:** [klm.labs.inc@gmail.com](mailto:klm.labs.inc@gmail.com)

eSign: Document Signer & Fill is made by KLM Labs. On your Home Screen it appears as **Signer**. It lets you sign, fill and stamp PDFs and scanned pages on your iPhone or iPad. This policy explains what stays on your device, what leaves it, who receives it and why.

## The short version

- **Your documents are stored on your device.** PDFs, scans, photos you import, your signatures and initials, and the text, dates and stamps you add are stored on your device. The app never uploads them to us or to anyone else, and screen recordings hide them (see below).
- **Signing in is optional.** From version 1.2.0 you can sign in with Apple or Google so KLM Labs can contact you about the app. The app works the same without an account, and signing in never uploads your documents or signatures. If you sign in, we get your email address and, if you share it, your name, and they are stored with Google Firebase (see "Signing in with Apple or Google"). Your usage and purchase records are kept together by random identifiers, so they are linked to you (see below).
- **Usage analytics with a random identifier.** The App Store version sends usage events, such as "a document was added", to PostHog, together with technical details about the app and device, and from version 1.2.0 a report when the app crashes. An approximate location (country and city) is worked out from your internet address, which PostHog does not store. No event ever includes a document, file name, signature or text you type.
- **Masked screen recordings, from version 1.1.0.** The App Store version also records the app's screens as you use them and where your touches start and end. Recordings are made only on iOS and iPadOS 26 or newer; on an older version the app records nothing. By design, all text, pages, signatures, initials, stamps and photos are covered by solid blocks on your iPhone or iPad before a recording is sent (our test recordings show this; see below), and recording pauses while Photos, Files, the share sheet or a touch-and-hold menu is open (see below).
- **Purchases are handled by Apple.** We never see your card or bank details. RevenueCat receives your App Store purchase records so the app can unlock and restore Signer Pro.
- **No ads and no tracking.** We do not sell data, show adverts, use an advertising identifier, or track you across other apps and websites.

## What is stored on your device

Everything you bring into the app and make with it stays on your device: imported PDFs and images, scanned pages, document names, the signatures and initials you draw or photograph, and everything you place on a page (signatures, initials, text, dates, check marks and stamps). They are kept in the app's own storage on your device and are not synced to iCloud by the app. None of it is sent to KLM Labs, PostHog or RevenueCat (screen recordings show it only as solid blocks; see "A masked recording of the app's screens" below), and we cannot see, retrieve or delete it. Like other app data, it is included in your device's backups (iCloud Backup or a computer backup) if you have backups turned on; those backups are controlled by Apple and your settings, not by us.

The app also keeps your settings and its last check of your plan on your device.

## Camera and photos

- **Camera.** The app asks for camera access only when you scan a document or photograph a signature on paper. It uses Apple's document scanner, and the pages or signature are processed on your device. You can turn camera access off in Settings; everything else still works.
- **Photos.** When you import from Photos, the system shows its own picker and the app receives only the photos you choose. The app does not ask for access to your photo library.
- **Files and "Open in".** Files you choose in the Files picker, or send to Signer from another app, are copied into the app on your device.

## Signing in with Apple or Google

From version 1.2.0 the app offers sign-in with Apple or Google: on a page before the plans screen or as a small card on the Documents screen, at most twice in all, and any time in **Settings → Account**. Signing in is optional. Tap **Continue** under the two sign-in buttons to skip it, or close the card; every feature, purchase and free trial works the same without an account. Signing in does not upload, back up or sync your documents or signatures: they stay on your device as described above.

**What we get.** If you sign in, Apple or Google gives the app your email address and, if you share it, your name. You never type them. If you sign in with Apple and choose **Hide My Email**, we get Apple's private relay address instead of your own.

**Where it is kept.** Your email address and name are stored with Google Firebase Authentication, in a project run by KLM Labs; Google processes them for us. Firebase also keeps whether you used Apple or Google, and when you first and last signed in. There is no separate backup. Apple or Google handles the sign-in itself under its own privacy policy.

**Why.** Only so KLM Labs (Mayank, who makes the app) can contact you about the app: if something breaks, or to hear what you think. We never sell your email address or name, and we never use them for ads.

**Who never gets it.** Your email address and name are never sent to PostHog or RevenueCat. RevenueCat gets only a random account ID that links your purchases to your account, and whether the app came from the App Store or TestFlight. RevenueCat passes that account ID on to PostHog with the purchase events described below, so we can match those events to your account.

**Our list.** To see which app you signed in from and whether you have Signer Pro, KLM Labs can export the list from Firebase, joined with RevenueCat's purchase records, to one file. Each export replaces the last one. It is the only other copy.

**Deleting your account.** In the app, open **Settings → Account → Delete my account** and confirm. With Apple, the app asks you to confirm once more. Then it deletes your account from Firebase. If you signed in with Apple, it also revokes the app's access to your Apple Account; if that step fails, the app tells you, and you can remove the app under Sign in with Apple in your Apple Account settings. If you signed in with Google, it disconnects the app from your Google Account. It also removes the account ID from your purchase record at RevenueCat and the sign-in details stored on your device. Deleting your account does not cancel a subscription, and your documents and signatures stay on your device. Deleting the app does not delete your account. You can also email [klm.labs.inc@gmail.com](mailto:klm.labs.inc@gmail.com) and we will delete it.

## Product analytics (PostHog)

We use product analytics to learn which features are used and where people get stuck, so we can improve the app. [PostHog, Inc.](https://posthog.com/privacy) processes the analytics for KLM Labs on servers in the United States. Analytics, and from version 1.1.0 masked screen recordings, are sent only by the App Store version of the app (and TestFlight test builds); there is no setting for them in the app.

### What analytics collects

**Events describing what you did, never what your documents contain.** The app sends these events: the app was opened; a document was added (from Files, Photos, the scanner or "Open in"); an item was placed on a page (which kind: signature, initials, text, date, check mark or stamp); a signature or initials was saved (drawn or from a photo); a signed document was shared, saved or the share was cancelled; the plans screen was shown or closed (and where it was opened from); and the result of a purchase or restore (which plan, Yearly or Lifetime, and whether it completed, was cancelled, failed, restored or found nothing). From version 1.2.0 it also sends events about signing in, never your email address or name: that the sign-in page, the sign-in card on the Documents screen or the Account section in Settings was shown; that you signed in, skipped, cancelled, or that it failed (with the kind of failure, such as no connection); whether you chose Apple or Google; whether Apple gave a private relay address and whether an email address came back; and that you deleted your account, or that deleting it failed (and why). **No event ever contains a document, a page, a file or document name, a signature, a stamp word or any text you type.**

**Technical details** that the analytics software adds to each event: the app's name, version and build; the device maker, model and type; the iOS or iPadOS version; the screen size; your language, region and time zone settings; whether the device is on Wi-Fi or cellular data; whether the app came from TestFlight; the analytics software's name and version; the time of the event; and random event and session identifiers. They also include the app's bundle identifier, the operating system's name, the generic device name the system reports (such as "iPhone" or "iPad"), and whether the app is running in a simulator or was installed from outside the App Store.

**A random identifier** that PostHog creates on your device. It lets PostHog count events from the same installation. It is not your name, email, phone number, Apple Account or the device's advertising identifier. The app also gives it to RevenueCat, so your usage and purchases can be matched (see below). If you sign in, it can also be matched to your account through the account ID described under "Signing in with Apple or Google".

**An approximate location.** Like any internet service, PostHog sees the IP address your device connects from. PostHog uses that IP address to estimate a country and city when the events arrive, and is set to discard it instead of storing it with the events. **The app does not ask for location permission and never reads your device's GPS.**

**Purchase events.** The app gives RevenueCat the same random identifier. When you start a trial, buy, renew, cancel or when a plan expires, RevenueCat sends a record of that event (for example the product, its price, RevenueCat's app user ID and Apple's transaction ID) to PostHog under that identifier, so we can see how the plans are used. From version 1.2.0, if you sign in, these records also carry your random account ID. See "Purchases and subscriptions" below.

**A masked recording of the app's screens, from version 1.1.0.** So we can see where people get stuck and where they give up, the app records its screens while you use it: screenshots of the app's own screens, taken as they change, and where each touch starts and ends. Recordings are made only on iOS and iPadOS 26 or newer; on an older version the app records nothing. A recording can include any screen of the app. Masking is done by the app on your device, before a recording is sent: every masking option of the recording software is turned on, and the app adds its own solid block over everything it draws from your documents and signatures. So far we have checked test recordings of version 1.1.0 made on iPhone and iPad simulators (iOS 26). In them, the signature pad while a signature is being drawn, a signature from a photo, a document being signed with a signature and a stamp placed, the signed document ready to share, the documents list, the plans screen and the saved signatures in Settings appear as the table below says or fully blocked, and nothing was recorded while the photo picker or the share screen was open. This is what the app is built to show:

| In a recording | What it shows |
|---|---|
| Hidden by solid blocks | All text on screen (document names, titles, buttons, prices, text you type or place on a page, and from version 1.2.0 the email address Settings shows when you are signed in); every document page and page thumbnail, also while you zoom; signatures and initials, whether drawn, from a photo, saved or placed; stamps, dates and check marks on a page; photos and the scanner's camera view |
| Not recorded | The Photos and Files pickers, the share sheet, Save to Files, and the touch-and-hold menu of a document or a saved signature: recording pauses while one is open and starts again a second after it closes |
| Visible | Each screen's layout and colors, small symbols (such as the gear and the + button), the app's own icon on the plans screen, the ink color choices, which option is selected, and where each touch starts and ends |
| Your touches | Only where a touch starts and where it ends. A stroke on the signature pad is two points, never its path, so it does not record your signature. Repeated fast taps are not recorded as a separate event |

A recording carries the same random identifier and session identifier as your analytics events, so it is linked to you in the same way. Console output and network activity are not recorded. Masking is a technical measure applied on the device, and we treat any change to what a recording shows or masks as a change to this policy.

**Crash reports, from version 1.2.0.** If the app crashes, it saves a report on your device and sends it to PostHog the next time you open the app. Crash reports: the type of crash, where in the app's code it happened, the error message, your device model, iOS or iPadOS and app versions, and the same random install id as our other events, so a report is linked to you in the same way. A crash report never contains a document, a page, a scan, a photo or a signature. We write our own error messages to name what went wrong, not what you typed or saved. A message from iOS or a library we use could still include part of it, such as a document's name. We use crash reports only to find and fix crashes, not for usage analytics.

### What analytics never collects

Analytics never collects your name, email address, phone number, contacts or precise location. If you sign in, your email address and name go to Google Firebase, never to PostHog (see "Signing in with Apple or Google"). No analytics event contains your documents, scans, photos, signatures, file names or anything you type; screen recordings hide them as described above.

## Purchases and subscriptions (Apple and RevenueCat)

The app is paid: Signer Pro is offered as a yearly subscription with a free trial for eligible new subscribers, or as a one-time Lifetime purchase. Payments are made through Apple's App Store with your Apple Account. **Apple processes the payment; KLM Labs never receives or stores your card or bank details.**

[RevenueCat, Inc.](https://www.revenuecat.com/privacy) processes purchase records for KLM Labs so the app can check whether you have Signer Pro, unlock it and restore it on another iPhone or iPad. RevenueCat receives your App Store purchase and subscription records (the product, Apple's transaction IDs, dates, trial and renewal status), a random app user ID that RevenueCat creates (signing in does not change it), which set of plans the app showed you, technical details such as the app version, iOS or iPadOS version and App Store country, and the random PostHog identifier described above so purchase events can be matched with usage analytics. From version 1.2.0, if you sign in, it also receives your random account ID and whether the app came from the App Store or TestFlight, never your email address or name. RevenueCat also receives your IP address when the app connects to it, and your device's vendor ID (IDFV) when the system provides one. iOS and iPadOS give each app developer one vendor ID per device, the same in all of that developer's apps; it is not the advertising identifier.

We use purchase records only to provide and restore Signer Pro, to understand how the plans are used, and to handle your requests. We do not use them for advertising.

## Reminders and notifications

Before the plans screen, if you can get the free trial and haven't answered before, the app shows a page about the trial and asks for permission to send notifications. If you allow them and your trial is set to renew, the app schedules a reminder on your device for 2 days before the trial ends, and removes it if you cancel or the trial ends. The reminder is not sent from a server, and no push token is sent to us. You can say no, or turn notifications off later in Settings; the app works the same either way.

## Sharing and saving documents

When you share or save a signed document, the app makes a flattened copy on your device and opens the system share sheet or the Files picker. The document leaves your device only if you choose a destination, which then handles it under its own privacy practices. After a completed share or save, the app may ask the system to show Apple's rating prompt, at most once per app version.

## When you email us

If you email us for support or a privacy request, we receive your email address, your name if your email includes it, your message and any attachments you choose to send, such as screenshots. Google processes this mail for us through Gmail. We use it only to answer and handle your request.

## Service providers

PostHog, RevenueCat and Google (Firebase Authentication, for sign-in, and Gmail, for email) process data for KLM Labs. We require the service providers that receive personal data from us to protect it at the same or an equivalent level as this policy describes and Apple's App Review Guidelines require. We do not sell personal data or share it for advertising.

## How long data is kept

Documents and signatures on your device stay until you delete them in the app or delete the app; copies in your backups, and anything you shared, are managed separately.

We keep analytics events, crash reports, screen recordings, purchase records and support emails only as long as we need them to run, support and improve the app, or as the law requires (for example, purchase records for tax and accounting), and then delete them. Deleting the app does not delete records already sent to PostHog or RevenueCat; to ask us to delete them, see "Your choices and rights" below.

If you sign in, your account (email address, name, whether you used Apple or Google, and your sign-in dates) is kept in Firebase until you delete it or ask us to. A deleted account leaves Firebase at once, and our exported file the next time we export it; a file made before you deleted your account can hold your address until then. When you ask us by email, we delete the account and replace the file. Records already sent to PostHog and RevenueCat keep the random account ID, but once your account and that file are gone, nothing links it to your email address.

## Children

Signer is a tool for signing documents and is not directed to children. We do not knowingly collect personal information from children. If you believe a child has used the app, contact us and we will delete any records we can find.

## Your choices and rights

- **Delete a document** from the Documents list, and a saved signature in **Settings → My signatures**, or delete the app to remove everything it stored.
- **Delete your account**, if you signed in: **Settings → Account → Delete my account** in the app, or email [klm.labs.inc@gmail.com](mailto:klm.labs.inc@gmail.com) and we will delete it (see "Signing in with Apple or Google").
- **Turn off camera access or reminders** in your device's Settings.
- **Cancel a subscription** in your Apple Account settings; see the [terms of use](/pdf-esign/terms/). Deleting the app does not cancel it.
- **Ask us to delete analytics records (events, crash reports and recordings) or purchase records.** Email [klm.labs.inc@gmail.com](mailto:klm.labs.inc@gmail.com). Because these records use random identifiers, tell us roughly when you used the app and, for purchases, when you bought, so we can find them. If you signed in, the email address Settings shows helps us find them too. We will tell you what we could find and delete. Apple keeps its own purchase records.
- **Ask what we hold** by emailing the same address.

Depending on where you live, you may have further rights over personal data, such as access, correction, deletion and objection. Contact us and we will respond as the law requires.

## Changes to this policy

If the app's data practices change, we will update this policy and the App Store privacy details before that version is released. The effective date at the top shows the latest change. 2026-10-21: masked screen recordings, from version 1.1.0 (see "Product analytics"). 2026-11-03: optional sign-in with Apple or Google, and crash reports, from version 1.2.0 (see "Signing in with Apple or Google" and "Product analytics"). Questions: [klm.labs.inc@gmail.com](mailto:klm.labs.inc@gmail.com).
