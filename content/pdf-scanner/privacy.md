# PDF Scanner App: OCR & Search Privacy Policy

**Effective date:** 2026-11-03

**Contact:** [klm.labs.inc@gmail.com](mailto:klm.labs.inc@gmail.com)

PDF Scanner App: OCR & Search is made by KLM Labs for iPhone and iPad. On your Home Screen it appears as **PDF Scanner**. It scans paper into PDFs on your iPhone or iPad, reads the text on each page, and lets you search, organize and share your scans. This policy explains what is kept on your device, what leaves it, who receives it and why.

## The short version

- **Your scans are kept on your device, and the app never uploads them.** Scanning and text recognition run on your iPhone or iPad. Pages, the text read from them, document and folder names are stored in the app on your device, and screen recordings hide them (see below).
- **Signing in is optional.** From version 1.1.0 you can sign in with Apple or Google so KLM Labs can contact you about the app. The app works the same without an account, and signing in never uploads your scans or their text. If you sign in, we get your email address and, if you share it, your name, and they are stored with Google Firebase (see "Signing in with Apple or Google"). Your identifiers, usage data, purchase records and approximate location are linked to you (see below).
- **Usage analytics with a random identifier.** The App Store version sends usage events, such as "a scan was saved" with its page count, to PostHog, together with technical details about the app and device, and from version 1.1.0 a report when the app crashes. An approximate location (country and city) is worked out from your internet address, which PostHog does not store. No usage event ever includes a page, text, image or document name; a crash report's error message could still include part of one, such as a document's name (see "Crash reports").
- **Masked screen recordings, from version 1.1.0.** The App Store version also records the app's screens as you use them and where your touches start and end. Recordings are made only on iOS and iPadOS 26 or newer; on an older version the app makes no screen recordings. In our test recordings, text and every page, thumbnail and recognized text appeared as solid blocks. Nothing was recorded while Photos, the share sheet, Save to Files or a touch-and-hold menu was open, or while an iPad turned (see below).
- **Purchases are handled by Apple.** We never see your card or bank details. RevenueCat receives your App Store purchase records so the app can unlock and restore your plan.
- **No ads and no tracking.** We do not sell data, show adverts, use an advertising identifier, or track you across other apps and websites.
- **In the App Store's privacy details,** the app lists nine types of data from version 1.1.0, all linked to you and none used for tracking: User ID, Device ID, Product Interaction, Other Usage Data, Purchase History, Coarse Location, Crash Data, and, if you sign in, Email Address and Name.

## What is kept on your device

Your scanned pages and imported photos, the filter and rotation of each page, the text read from each page, document and folder names, and your settings (such as the default filter and your last export choices) are stored in the app's own storage on your iPhone or iPad. The app does not sync them to iCloud or to any server of ours. The app sends none of it to KLM Labs, PostHog or RevenueCat (a crash report's error message is the one exception; see "Crash reports"), and we cannot see, retrieve or delete it.

Like other app data, your library is included in your device's backups (iCloud Backup or a computer backup) if you have backups turned on. Those backups are controlled by Apple and your settings, not by us.

## Camera, photos and text recognition

- **Camera.** The app asks for camera access the first time you tap Scan. It uses Apple's document scanner, and the pages are processed on your device. You can turn camera access off in Settings; importing from Photos still works.
- **Photos.** When you import from Photos, iOS shows its own picker and the app receives only the photos you choose. The app never asks to see your photo library. If you share a document as JPGs and save them to Photos, iOS first asks whether the app may add photos; that permission only adds images and does not let the app see your library.
- **Text recognition.** Each page is read by Apple's on-device text recognition, so the text can be searched and copied. The text stays with the document on your device.

## Signing in with Apple or Google

From version 1.1.0 the app offers sign-in with Apple or Google: on a page before the plans screen or as a small card on the Library, at most twice in all, and any time in **Settings → Account**. Signing in is optional. Tap **Continue** under the two sign-in buttons to skip it, or close the card; every feature, plan and free trial works the same without an account. Signing in does not upload, back up or sync your scans, their text or your document and folder names: they are kept on your device as described above.

**What we get.** If you sign in, Apple or Google gives the app your email address and, if you share it, your name. You never type them. If you sign in with Apple and choose **Hide My Email**, we get Apple's private relay address instead of your own.

**Where it is kept.** Your email address and name are stored with Google Firebase Authentication, in a project run by KLM Labs; Google processes them for us. Firebase also keeps whether you used Apple or Google, and when you first and last signed in. There is no separate backup. Apple or Google handles the sign-in itself under its own privacy policy.

**Why.** Only so KLM Labs (Mayank, who makes the app) can contact you about the app: if something breaks, or to hear what you think. We never sell your email address or name, and we never use them for ads.

**Who never gets it.** Your email address and name are never sent to PostHog or RevenueCat. RevenueCat gets only a random account ID that links your purchases to your account, and, when the app can tell, whether it came from the App Store or TestFlight. When RevenueCat passes purchase events on to PostHog (see "Purchase events" below), they carry that account ID too, so we can match those events to your account.

**Our list.** To see which app you signed in from and whether you have a plan, KLM Labs can export the list from Firebase, joined with RevenueCat's purchase records, to one file. Each export replaces the last one. It is the only other copy.

**Deleting your account.** In the app, open **Settings → Account → Delete my account** and confirm. The app may ask you to confirm with Apple or Google once more. Then it deletes your account from Firebase. If you signed in with Apple, it also revokes the app's access to your Apple Account; if that step fails, the app tells you, and you can remove the app under Sign in with Apple in your Apple Account settings. If you signed in with Google, it disconnects the app from your Google Account. It also removes the account ID from your purchase record at RevenueCat and the sign-in details stored on your device. Deleting your account does not cancel a subscription, and it does not touch your documents. Deleting the app does not delete your account. You can also email [klm.labs.inc@gmail.com](mailto:klm.labs.inc@gmail.com) and we will delete it.

## Product analytics (PostHog)

We use product analytics to learn which features are used and where people get stuck, so we can improve the app. [PostHog, Inc.](https://posthog.com/privacy) processes the analytics for KLM Labs on servers in the United States. Analytics, and from version 1.1.0 masked screen recordings and crash reports, are sent only by the App Store version of the app (and TestFlight test builds); there is no setting for them in the app.

### What analytics collects

**Events describing what you did, never what your scans contain.** Events record actions such as opening the app, saving a scan (with the number of pages), sharing or saving a document (and whether as a PDF or JPG), seeing or closing the plans screen, and the result of a purchase or restore (which plan, and whether it completed, was cancelled, failed or restored). From version 1.1.0 they also record signing in, never your email address or name: that the sign-in page, the sign-in card on the Library or the Account section in Settings was shown; that you signed in, skipped, cancelled, or that it failed (with the kind of failure, such as no connection); whether you chose Apple or Google; whether Apple gave a private relay address and whether an email address came back; and that you deleted your account, or that deleting it failed (and why). Every property the app itself adds to an event is a count, a choice from a fixed list, or a yes/no; the analytics software adds the identifiers and technical details described below. **No usage event ever contains a page, an image, recognized text, a search, a document or folder name, or a password.** A crash report's error message is the one exception: it could still include part of a document's name (see "Crash reports, from version 1.1.0").

**Technical details** that the analytics software adds to each event: the app's name, version and build; the device maker, model and type; the iOS version; the screen size; your language, region and time zone settings; whether the device is on Wi-Fi or cellular data; whether the app came from TestFlight; the analytics software's name and version; the time of the event; and random event and session identifiers. They also include the app's bundle identifier, the operating system's name, the generic device name iOS reports (such as "iPhone" or "iPad"), and whether the app is running in a simulator or was installed from outside the App Store.

**A random identifier** that PostHog creates on your device. It lets PostHog count events from the same installation. It is not your name, email, phone number, Apple Account or the device's advertising identifier. The app may also give it to RevenueCat, so your usage and purchases can be matched (see below). If you sign in, purchase events can also be matched to your account through the account ID described under "Signing in with Apple or Google".

**An approximate location.** Like any internet service, PostHog sees the IP address your device connects from. PostHog uses that IP address to estimate a country and city when the events arrive, and is set to discard it instead of storing it with the events. **The app does not ask for location permission and never reads your device's GPS.**

**Purchase events.** The app may give RevenueCat the same random identifier, so RevenueCat can send records of purchase events (for example a trial starting, a renewal or a cancellation, with the product, its price, RevenueCat's app user ID and Apple's transaction ID) to PostHog under it, and we can see how the plans are used. From version 1.1.0, if you sign in, these records also carry your random account ID. See "Purchases and subscriptions" below.

**Crash reports, from version 1.1.0.** If the app crashes, it saves a report on your device and sends it to PostHog the next time you open the app. Crash reports: the type of crash, where in the app's code it happened, the error message, your device model, iOS or iPadOS and app versions, and the same random install id as our other events, so a report is linked to you in the same way. The app puts none of your scans, pages, photos, recognized text or searches into a crash report. We write our own error messages to name what went wrong, not what you typed or saved. A message from iOS or a library we use could still include part of it, such as a document's name. We use crash reports only to find and fix crashes, not for usage analytics.

### Masked screen recordings (from version 1.1.0)

So we can see where people get stuck, the app records its screens while you use it: screenshots of the app's own screens, taken as they change, and where each touch starts and ends. **Recordings are made only on iOS and iPadOS 26 or newer; on an older version the app makes no screen recordings** (it still sends the analytics events above). A recording can include any screen of the app. Masking is done by the app on your device, before a recording is sent: every masking option of the recording software is on, and the app adds its own solid block over each page, thumbnail and the recognized text, and from version 1.1.0 over the email address Settings shows when you are signed in. A recording carries the same random identifier and session identifier as your analytics events, so it is linked to you in the same way. Console output and network activity are not recorded.

We checked test recordings of version 1.1.0 made on iPhone and iPad simulators (iOS 26), past the plans screen: the documents list and its tiles, a folder, a search, reviewing and editing pages, a document's pages and its recognized text, renaming a document and opening the menu under its name, deleting, moving and merging documents, the share options with a password typed, Settings and the plans screen; on iPad also turned between portrait, landscape and upside down (no frame was recorded during a turn). What a recording shows while a pointer rests over a document or a search result on iPad has not been tested. This is what they showed:

| In a recording | What it shows |
|---|---|
| Solid blocks | All text on screen (document and folder names, titles, buttons, prices and search text); every page and page thumbnail; the recognized text and the page crops in search results |
| Not recorded | The Photos picker, the share sheet, Save to Files and a document's touch-and-hold menu: recording pauses while one is open and starts again a second after it closes. While an iPad turns, recording pauses until the screen has held still. The Rename box did not appear in the recording, nor the name typed in it, and nothing changed in the recording while the share password was typed |
| Visible | Each screen's layout and colors, small symbols (such as the gear and the + button), the app's own illustrations, which option is selected, and where each touch starts and ends |

The app also pauses recording while an iPad's window changes size (Split View, Stage Manager); our simulator tests could not resize a window, so no test recording shows this yet. Our test recordings could not show the scanner's camera, as simulators have none. We treat any change to what a recording shows or masks as a change to this policy.

### What analytics never collects

Analytics never collects your name, email address, phone number, contacts or precise location. If you sign in, your email address and name go to Google Firebase, never to PostHog (see "Signing in with Apple or Google"). No usage event contains your scans, photos, recognized text, searches, file names or anything you type; screen recordings hide them, and a crash message from iOS or a library could still include part of one, as described above.

## Purchases and subscriptions (Apple and RevenueCat)

The app needs a plan: a yearly subscription with a free trial for eligible new subscribers, or a one-time Lifetime purchase. Payments are made through Apple's App Store with your Apple Account. **Apple processes the payment; KLM Labs never receives or stores your card or bank details.**

[RevenueCat, Inc.](https://www.revenuecat.com/privacy) processes purchase records for KLM Labs so the app can check whether you have access, unlock it and restore it on another iPhone or iPad. RevenueCat receives your App Store purchase and subscription records (the product, Apple's transaction IDs, dates, trial and renewal status), a random app user ID that RevenueCat creates (signing in does not change it), which set of plans the app showed you, technical details such as the app version, iOS version and App Store country, and, if the link described above is on, the random PostHog identifier. From version 1.1.0, if you sign in, it also receives your random account ID and, when the app can tell, whether it came from the App Store or TestFlight, never your email address or name. RevenueCat also receives your IP address when the app connects to it, and your device's vendor ID (IDFV) when iOS provides one. iOS gives each app developer one vendor ID per device, the same in all of that developer's apps; it is not the advertising identifier.

We use purchase records only to provide and restore your plan, to understand how the plans are used, and to handle your requests. We do not use them for advertising.

## Reminders and notifications

Before the plans screen, if you can get the free trial and haven't answered before, the app shows a page about the trial and asks for permission to send notifications. If you allow them and your trial is set to renew, the app schedules a reminder on your device for 2 days before the trial ends, and removes it if you cancel or the trial ends. The reminder is not sent from a server, and no push token is sent to us. You can say no, or turn notifications off later in Settings; the app works the same either way.

## Sharing documents

When you share or save a document, the app makes the PDF or JPG on your device and opens the system share sheet or the Files picker. If you add a password to a PDF, it is applied on your device and is not sent to us. The file leaves your device only if you choose a destination, which then handles it under its own privacy practices.

## When you email us

If you email us for support or a privacy request, we receive your email address, your name if your email includes it, your message and any attachments you choose to send, such as screenshots. Google processes this mail for us through Gmail. We use it only to answer and handle your request.

## Service providers

PostHog, RevenueCat and Google (Firebase Authentication, for sign-in, and Gmail, for email) process data for KLM Labs. We require the service providers that receive personal data from us to protect it at the same or an equivalent level as this policy describes and Apple's App Review Guidelines require. We do not sell personal data or share it for advertising.

## How long data is kept

Documents on your device stay until you delete them in the app or delete the app; copies in your backups, and anything you shared, are managed separately.

We keep analytics events, crash reports, screen recordings, purchase records and support emails only as long as we need them to run, support and improve the app, or as the law requires (for example, purchase records for tax and accounting), and then delete them. Deleting the app does not delete records already sent to PostHog or RevenueCat; to ask us to delete them, see "Your choices and rights" below.

If you sign in, your account (email address, name, whether you used Apple or Google, and your sign-in dates) is kept in Firebase until you delete it or ask us to. A deleted account leaves Firebase at once, and our exported file the next time we export it; a file made before you deleted your account can hold your address until then. When you ask us by email, we delete the account and replace the file. Records already sent to PostHog, including purchase events RevenueCat passed on, keep the random account ID, but once your account and that file are gone, nothing links it to your email address.

## Children

PDF Scanner is a tool for scanning documents and is not directed to children. We do not knowingly collect personal information from children. If you believe a child has used the app, contact us and we will delete any records we can find.

## Your choices and rights

- **Delete a document** in the app, or delete the app to remove everything it stored. Deleting a folder moves its documents out of the folder; it does not delete them.
- **Delete your account**, if you signed in: **Settings → Account → Delete my account** in the app, or email [klm.labs.inc@gmail.com](mailto:klm.labs.inc@gmail.com) and we will delete it (see "Signing in with Apple or Google").
- **Turn off camera access, adding photos or reminders** in your device's Settings.
- **Cancel a subscription** in your Apple Account settings; see the [terms of use](/pdf-scanner/terms/). Deleting the app does not cancel it.
- **Ask us to delete analytics records (events, crash reports and recordings) or purchase records.** Email [klm.labs.inc@gmail.com](mailto:klm.labs.inc@gmail.com). Because these records use random identifiers, tell us roughly when you used the app and, for purchases, when you bought, so we can find them. If you signed in, the email address Settings shows helps us find them too. We will tell you what we could find and delete. Apple keeps its own purchase records.
- **Ask what we hold** by emailing the same address.

Depending on where you live, you may have further rights over personal data, such as access, correction, deletion and objection. Contact us and we will respond as the law requires.

## Changes to this policy

If the app's data practices change, we will update this policy and the App Store privacy details before that version is released. The effective date at the top shows the latest change. 2026-10-22: masked screen recordings, from version 1.1.0 (see "Product analytics"). 2026-11-03: optional sign-in with Apple or Google, and crash reports, from version 1.1.0 (see "Signing in with Apple or Google" and "Product analytics"). Questions: [klm.labs.inc@gmail.com](mailto:klm.labs.inc@gmail.com).
