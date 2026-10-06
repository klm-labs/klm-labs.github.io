# PDF Scanner App: OCR & Search Privacy Policy

**Effective date:** 2026-10-06

**Contact:** [klm.labs.inc@gmail.com](mailto:klm.labs.inc@gmail.com)

PDF Scanner App: OCR & Search is made by KLM Labs. On your Home Screen it appears as **PDF Scanner**. It scans paper into PDFs on your iPhone, reads the text on each page, and lets you search, organize and share your scans. This policy explains what is kept on your device, what leaves it, who receives it and why.

## The short version

- **Your scans are kept on your device, and the app never uploads them.** Scanning and text recognition run on your iPhone. Pages, the text read from them, document and folder names are stored in the app on your iPhone.
- **There is no account and no sign-up.** The app never asks for your name or email address. Your identifiers, usage data, purchase records and approximate location are linked to you (see below).
- **Usage analytics with a random identifier.** The App Store version sends usage events, such as "a scan was saved" with its page count, to PostHog, together with technical details about the app and device. An approximate location (country and city) is worked out from your internet address, which PostHog does not store. No page, text, image or document name is ever included.
- **Purchases are handled by Apple.** We never see your card or bank details. RevenueCat receives your App Store purchase records so the app can unlock and restore your plan.
- **No ads and no tracking.** We do not sell data, show adverts, use an advertising identifier, or track you across other apps and websites.
- **In the App Store's privacy details,** the app lists six types of data, all linked to you and none used for tracking: User ID, Device ID, Product Interaction, Other Usage Data, Purchase History and Coarse Location.

## What is kept on your device

Your scanned pages and imported photos, the filter and rotation of each page, the text read from each page, document and folder names, and your settings (such as the default filter and your last export choices) are stored in the app's own storage on your iPhone. The app does not sync them to iCloud or to any server of ours. None of it is sent to KLM Labs, PostHog or RevenueCat, and we cannot see, retrieve or delete it.

Like other app data, your library is included in your iPhone's backups (iCloud Backup or a computer backup) if you have backups turned on. Those backups are controlled by Apple and your settings, not by us.

## Camera, photos and text recognition

- **Camera.** The app asks for camera access the first time you tap Scan. It uses Apple's document scanner, and the pages are processed on your iPhone. You can turn camera access off in Settings; importing from Photos still works.
- **Photos.** When you import from Photos, iOS shows its own picker and the app receives only the photos you choose. The app never asks to see your photo library. If you share a document as JPGs and save them to Photos, iOS first asks whether the app may add photos; that permission only adds images and does not let the app see your library.
- **Text recognition.** Each page is read by Apple's on-device text recognition, so the text can be searched and copied. The text stays with the document on your iPhone.

## Product analytics (PostHog)

We use product analytics to learn which features are used and where people get stuck, so we can improve the app. [PostHog, Inc.](https://posthog.com/privacy) processes the analytics for KLM Labs on servers in the United States. Analytics are sent only by the App Store version of the app (and TestFlight test builds); there is no analytics setting in the app.

### What analytics collects

**Events describing what you did, never what your scans contain.** Events record actions such as opening the app, saving a scan (with the number of pages), sharing or saving a document (and whether as a PDF or JPG), seeing or closing the plans screen, and the result of a purchase or restore (which plan, and whether it completed, was cancelled, failed or restored). Every property the app itself adds to an event is a count, a choice from a fixed list, or a yes/no; the analytics software adds the identifiers and technical details described below. **No event ever contains a page, an image, recognized text, a search, a document or folder name, or a password.**

**Technical details** that the analytics software adds to each event: the app's name, version and build; the device maker, model and type; the iOS version; the screen size; your language, region and time zone settings; whether the device is on Wi-Fi or cellular data; whether the app came from TestFlight; the analytics software's name and version; the time of the event; and random event and session identifiers. They also include the app's bundle identifier, the operating system's name, the generic device name iOS reports (such as "iPhone"), and whether the app is running in a simulator or was installed from outside the App Store.

**A random identifier** that PostHog creates on your device. It lets PostHog count events from the same installation. It is not your name, email, phone number, Apple Account or the device's advertising identifier. The app may also give it to RevenueCat, so your usage and purchases can be matched (see below).

**An approximate location.** Like any internet service, PostHog sees the IP address your device connects from. PostHog uses that IP address to estimate a country and city when the events arrive, and is set to discard it instead of storing it with the events. **The app does not ask for location permission and never reads your device's GPS.**

**Purchase events.** The app may give RevenueCat the same random identifier, so RevenueCat can send records of purchase events (for example a trial starting, a renewal or a cancellation, with the product, its price, RevenueCat's app user ID and Apple's transaction ID) to PostHog under it, and we can see how the plans are used. See "Purchases and subscriptions" below.

### What analytics never collects

We do not collect your name, email address, phone number, contacts, scans, photos, recognized text, searches, file names, precise location or anything you type. We do not record your screen, and we do not collect crash reports.

## Purchases and subscriptions (Apple and RevenueCat)

The app needs a plan: a yearly subscription with a free trial for eligible new subscribers, or a one-time Lifetime purchase. Payments are made through Apple's App Store with your Apple Account. **Apple processes the payment; KLM Labs never receives or stores your card or bank details.**

[RevenueCat, Inc.](https://www.revenuecat.com/privacy) processes purchase records for KLM Labs so the app can check whether you have access, unlock it and restore it on another iPhone. RevenueCat receives your App Store purchase and subscription records (the product, Apple's transaction IDs, dates, trial and renewal status), a random app user ID that RevenueCat creates (there is no login), which set of plans the app showed you, technical details such as the app version, iOS version and App Store country, and, if the link described above is on, the random PostHog identifier. RevenueCat also receives your IP address when the app connects to it, and your iPhone's vendor ID (IDFV) when iOS provides one. iOS gives each app developer one vendor ID per iPhone, the same in all of that developer's apps; it is not the advertising identifier.

We use purchase records only to provide and restore your plan, to understand how the plans are used, and to handle your requests. We do not use them for advertising.

## Reminders and notifications

Before the plans screen, if you can get the free trial and haven't answered before, the app shows a page about the trial and asks for permission to send notifications. If you allow them and your trial is set to renew, the app schedules a reminder on your iPhone for 2 days before the trial ends, and removes it if you cancel or the trial ends. The reminder is not sent from a server, and no push token is sent to us. You can say no, or turn notifications off later in Settings; the app works the same either way.

## Sharing documents

When you share or save a document, the app makes the PDF or JPG on your iPhone and opens the system share sheet or the Files picker. If you add a password to a PDF, it is applied on your iPhone and is not sent to us. The file leaves your device only if you choose a destination, which then handles it under its own privacy practices.

## When you email us

If you email us for support or a privacy request, we receive your email address, your name if your email includes it, your message and any attachments you choose to send, such as screenshots. Google processes this mail for us through Gmail. We use it only to answer and handle your request.

## Service providers

PostHog, RevenueCat and, for email, Google (Gmail) process data for KLM Labs. We require the service providers that receive personal data from us to protect it at the same or an equivalent level as this policy describes and Apple's App Review Guidelines require. We do not sell personal data or share it for advertising.

## How long data is kept

Documents on your device stay until you delete them in the app or delete the app; copies in your backups, and anything you shared, are managed separately.

We keep analytics events, purchase records and support emails only as long as we need them to run, support and improve the app, or as the law requires (for example, purchase records for tax and accounting), and then delete them. Deleting the app does not delete records already sent to PostHog or RevenueCat; to ask us to delete them, see "Your choices and rights" below.

## Children

PDF Scanner is a tool for scanning documents and is not directed to children. We do not knowingly collect personal information from children. If you believe a child has used the app, contact us and we will delete any records we can find.

## Your choices and rights

- **Delete a document** in the app, or delete the app to remove everything it stored. Deleting a folder moves its documents out of the folder; it does not delete them.
- **Turn off camera access, adding photos or reminders** in your iPhone's Settings.
- **Cancel a subscription** in your Apple Account settings; see the [terms of use](/pdf-scanner/terms/). Deleting the app does not cancel it.
- **Ask us to delete analytics or purchase records.** Email [klm.labs.inc@gmail.com](mailto:klm.labs.inc@gmail.com). Because these records use random identifiers rather than an account, tell us roughly when you used the app and, for purchases, when you bought, so we can find them. We will tell you what we could find and delete. Apple keeps its own purchase records.
- **Ask what we hold** by emailing the same address.

Depending on where you live, you may have further rights over personal data, such as access, correction, deletion and objection. Contact us and we will respond as the law requires.

## Changes to this policy

If the app's data practices change, we will update this policy and the App Store privacy details before that version is released. The effective date at the top shows the latest change. Questions: [klm.labs.inc@gmail.com](mailto:klm.labs.inc@gmail.com).
