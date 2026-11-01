# Flip Clock: Big Digital Alarm Privacy Policy

**Effective date:** 2026-11-02

**Contact:** [klm.labs.inc@gmail.com](mailto:klm.labs.inc@gmail.com)

Flip Clock: Big Digital Alarm is made by KLM Labs. On your Home Screen it appears as **Flip Clock**. It shows a big clock on your iPhone or iPad, rings alarms you set, and adds clock widgets to your Home Screen and Lock Screen. This policy explains what is kept on your device, what leaves it, who receives it and why.

## The short version

- **Your alarms are kept on your device.** Alarm times, repeat days and labels, your clock's look and your settings are stored in the app on your device. No analytics event contains them (analytics records only which clock face you choose), but from version 1.0.1 the screen recordings below show your alarm times and repeat days as they appear on screen; your alarm labels are masked.
- **Signing in is optional.** From version 1.1.0 you can sign in with Apple or Google so KLM Labs can contact you about the app. The app works the same without an account. If you sign in, we get your email address and, if you share it, your name, and they are stored with Google Firebase (see "Signing in with Apple or Google"). Your identifiers, usage data, purchase records and approximate location are linked to you (see below).
- **Usage analytics with a random identifier.** The App Store version sends usage events, such as "an alarm was saved" or "the clock face was changed", to PostHog, together with technical details about the app and device, and from version 1.1.0 a report when the app crashes. An approximate location (country and city) is worked out from your internet address, which PostHog does not store. No event ever includes an alarm time, repeat day or label.
- **Screen recordings, from version 1.0.1.** The App Store version also records the app's screens as you use them and where you tap. The recordings show the app's own words and numbers, including the clock, your alarm times and your settings; the alarm label you type, and from version 1.1.0 the email address Settings shows when you are signed in, are masked on your iPhone or iPad before a recording is sent (see below).
- **Purchases are handled by Apple.** We never see your card or bank details. RevenueCat receives your App Store purchase records so the app can unlock and restore your plan.
- **No ads and no tracking.** We do not sell data, show adverts, use an advertising identifier, or track you across other apps and websites.
- **In the App Store's privacy details,** the app lists these types of data, all linked to you and none used for tracking: User ID, Device ID, Product Interaction, Other Usage Data, Purchase History and Coarse Location; for the screen recordings from version 1.0.1, Other User Content; and from version 1.1.0, Crash Data for the crash reports and, if you sign in, Email Address and Name.

## What is kept on your device

Your alarms (time, repeat days, label, snooze length and whether each one is on), your clock's look (face, font, color, background, 12- or 24-hour time, and whether seconds, the date and the next alarm show), your brightness, night mode and keep-screen-on settings, and whether your plan is active (so the widgets know what to show) are stored in the app's own storage on your device, which the app's widgets can also read. The app does not sync them to iCloud or to any server of ours. No analytics event or purchase record contains your alarm times, repeat days or labels, and we cannot retrieve or delete them. From version 1.0.1, though, the screen recordings described under "A recording of the app's screens" show your alarm times and repeat days as they appear on screen (your labels are masked). The exceptions are described below: analytics records which clock face you choose and when an alarm is saved, and your plan's status comes from RevenueCat.

Like other app data, it is included in your device's backups (iCloud Backup or a computer backup) if you have backups turned on. Those backups are controlled by Apple and your settings, not by us.

## Alarms, the screen and the battery

- **Alarms.** iOS or iPadOS asks you whether the app may schedule alarms. Your alarms are scheduled with Apple's alarm system (AlarmKit) on your device. When one rings, the system shows it on the Lock Screen (and on iPhone in the Dynamic Island, in StandBy and on a paired Apple Watch). Apple's system handles this on your devices; no analytics event contains your alarm times, repeat days or labels (analytics records only that an alarm was saved or set again). If you turn alarm access off in Settings, the app's alarms are not scheduled and do not ring.
- **Keeping the screen on.** While the clock is on screen, the app can stop your device from locking, depending on your keep-screen-on setting. To do that it checks whether your device is charging. This check happens on your device and is not sent anywhere.
- **No other permissions.** The app does not ask for your camera, photos, microphone, contacts or location.

## Signing in with Apple or Google

From version 1.1.0 the app offers sign-in with Apple or Google: on a page before the plans screen, at most once more as a small card on the clock, and any time in **Settings → Account**. Signing in is optional. Tap **Continue** under the two sign-in buttons to skip it, or **Close** on the card; every feature, purchase and free trial works the same without an account.

**What we get.** If you sign in, Apple or Google gives the app your email address and, if you share it, your name. You never type them. If you sign in with Apple and choose **Hide My Email**, we get Apple's private relay address instead of your own.

**Where it is kept.** Your email address and name are stored with Google Firebase Authentication, in a project run by KLM Labs; Google processes them for us. Firebase also keeps whether you used Apple or Google, and when you first and last signed in. There is no separate backup. Apple or Google handles the sign-in itself under its own privacy policy.

**Why.** Only so KLM Labs (Mayank, who makes the app) can contact you about the app: if something breaks, or to hear what you think. We never sell your email address or name, and we never use them for ads.

**Who never gets it.** Your email address and name are never sent to PostHog or RevenueCat. RevenueCat gets only a random account ID that links your purchases to your account, and whether the app came from the App Store or TestFlight. RevenueCat passes that account ID on to PostHog with the purchase events described below, so we can match those events to your account.

**Our list.** To see which app you signed in from and whether you have a plan, KLM Labs can export the list from Firebase, joined with RevenueCat's purchase records, to one file. Each export replaces the last one. It is the only other copy.

**Deleting your account.** In the app, open **Settings → Account → Delete my account** and confirm. The app asks you to confirm with Apple or Google once more, then deletes your account from Firebase. If you signed in with Apple, it also revokes the app's access to your Apple Account; if that step fails, the app tells you, and you can remove the app under Sign in with Apple in your Apple Account settings. If you signed in with Google, it disconnects the app from your Google Account. It also removes the account ID from your purchase record at RevenueCat and the sign-in details stored on your device. Deleting your account does not cancel a subscription, and your alarms, look and settings stay on your device. Deleting the app does not delete your account. You can also email [klm.labs.inc@gmail.com](mailto:klm.labs.inc@gmail.com) and we will delete it.

## Product analytics (PostHog)

We use product analytics to learn which features are used and where people get stuck, so we can improve the app. [PostHog, Inc.](https://posthog.com/privacy) processes the analytics for KLM Labs on servers in the United States. Analytics, and from version 1.0.1 screen recordings, are sent only by the App Store version of the app (and TestFlight test builds); there is no setting for them in the app.

### What analytics collects

**Events describing what you did, never what your alarms say.** Events record actions such as opening the app, finishing the first-run screens, seeing the trial reminder page and your answer to the notification request, saving an alarm, the app setting an alarm again after it went missing, changing the clock face (which face only), seeing the plans screen, and the result of a purchase or restore (which plan, and whether it completed, was cancelled, failed or restored). From version 1.1.0 it also sends events about signing in, never your email address or name: that the sign-in page, the sign-in card on the clock or the Account section in Settings was shown; that you signed in, skipped, cancelled, or that it failed (with the kind of failure, such as no connection); whether you chose Apple or Google; whether Apple gave a private relay address and whether an email address came back; and that you deleted your account, or that deleting it failed (and why). Every property the app itself adds to an event is a count, a choice from a fixed list, or a yes/no; the analytics software adds the identifiers and technical details described below. Its own automatic events (screen views, taps on buttons, repeated quick taps on one spot) are turned off. **No event ever contains an alarm time, a repeat day or an alarm label.**

**Technical details** that the analytics software adds to each event: the app's name, version and build; the device maker, model and type; the iOS or iPadOS version; the screen size; your language, region and time zone settings; whether the device is on Wi-Fi or cellular data; whether the app came from TestFlight; the analytics software's name and version; the time of the event; and random event and session identifiers. They also include the app's bundle identifier, the operating system's name, the generic device name the system reports (such as "iPhone" or "iPad"), and whether the app is running in a simulator or was installed from outside the App Store.

**A random identifier** that PostHog creates on your device. It lets PostHog count events from the same installation. It is not your name, email, phone number, Apple Account or the device's advertising identifier. The app also gives it to RevenueCat, so your usage and purchases are linked (see below). If you sign in, it can also be matched to your account through the account ID described under "Signing in with Apple or Google".

**An approximate location.** Like any internet service, PostHog sees the IP address your device connects from. PostHog uses that IP address to estimate a country and city when the events arrive, and is set to discard it instead of storing it with the events. **The app does not ask for location permission and never reads your device's GPS.**

**Purchase events.** Because the app gives RevenueCat the same random identifier, RevenueCat sends records of purchase events (for example a trial starting, a renewal, a cancellation or a Lifetime purchase, with the product, its price, RevenueCat's app user ID and Apple's transaction ID) to PostHog under it, and we can see how the plans are used. From version 1.1.0, if you sign in, these records also carry your random account ID. See "Purchases and subscriptions" below.

**A recording of the app's screens, from version 1.0.1.** So we can see where people tap, what they struggle with and where they give up, the app records its screens while you use it: screenshots of the app's own screens, taken as they change, and where you tap. A recording can include any screen of the app. Recording stops after 5 minutes without a touch, such as when the clock is left on overnight, and starts again when you touch the screen or come back to the app. We checked what a recording shows on a test recording of version 1.0.1, made on a simulated iPhone: the first-run pages, the plans screen, the clock, Alarms (adding two alarms, one with a label), Look and Settings.

| In a recording | What it shows |
|---|---|
| Readable | The app's own words and numbers: titles, buttons, plan names and prices, the time and date on the clock face, the next-alarm line under it, your alarm times and repeat days, the alarm time picker, your Look choices, and your settings (such as the night schedule's times) |
| Masked | The alarm label you type: a solid block covers the Label box (before, while and after you type), and the line under an alarm's time in Alarms whenever it includes your label (the repeat days on that line are covered with it). From version 1.1.0, also the email address Settings shows when you are signed in. The app's icon on the plans screen and in Settings, and the small symbols on the plans screen, are covered by blocks too |
| Your taps | Where you tap (the position on the screen). The analytics software's separate event for repeated quick taps is turned off |
| Not in a recording | The keyboard, which is not part of the app's screen; iOS's own requests, such as the ones asking to allow notifications and alarms, did not appear in our recordings either |

The app shows no photos. Small symbols elsewhere may or may not be covered by a block (the one in the Alarms header stayed visible in our test).

A recording carries the same random identifier and session identifier as your analytics events, so it is linked to you in the same way. Console output and network activity are not recorded. We treat any change to what a recording shows or masks as a change to this policy.

**Crash reports, from version 1.1.0.** If the app crashes, it saves a report on your device and sends it to PostHog the next time you open the app. Crash reports: the type of crash, where in the app's code it happened, the error message, your device model, iOS or iPadOS and app versions, and the same random install id as our other events, so a report is linked to you in the same way. We write our own error messages to name what went wrong, not what you typed or saved. A message from iOS or a library we use could still include part of it. We use crash reports only to find and fix crashes, not for usage analytics.

### What analytics never collects

Analytics never collects your name, email address, phone number, contacts or precise location. If you sign in, your email address and name go to Google Firebase, never to PostHog (see "Signing in with Apple or Google"). No analytics event contains your alarm times, repeat days, alarm labels or anything you type; screen recordings show your alarm times and repeat days and mask your alarm labels, as described above.

## Purchases and subscriptions (Apple and RevenueCat)

The app needs a plan: a yearly subscription with a free trial for eligible new subscribers, or a one-time Lifetime purchase. Payments are made through Apple's App Store with your Apple Account. **Apple processes the payment; KLM Labs never receives or stores your card or bank details.**

[RevenueCat, Inc.](https://www.revenuecat.com/privacy) processes purchase records for KLM Labs so the app can check whether you have access, unlock it and restore it on another iPhone or iPad. RevenueCat receives your App Store purchase and subscription records (the product, Apple's transaction IDs, dates, trial and renewal status), a random app user ID that RevenueCat creates (signing in does not change it), which set of plans the app showed you, technical details such as the app version, iOS or iPadOS version and App Store country, and the random PostHog identifier. From version 1.1.0, if you sign in, it also receives your random account ID and whether the app came from the App Store or TestFlight, never your email address or name. RevenueCat also receives your IP address when the app connects to it, and your device's vendor ID (IDFV) when the system provides one. iOS and iPadOS give each app developer one vendor ID per device, the same in all of that developer's apps; it is not the advertising identifier.

We use purchase records only to provide and restore your plan, to understand how the plans are used, and to handle your requests. We do not use them for advertising.

## Reminders and notifications

The first time you open the app, before the plans screen, it shows a page about the free trial if the plan it suggests has one, you are eligible, and you haven't refused notifications. If you haven't answered before, its **Continue** button asks for permission to send notifications. If you allow them and your trial is set to renew, the app schedules a reminder on your device for 2 days before the trial ends, and removes it if you cancel, buy or restore another plan, or the trial ends. The reminder is not sent from a server, and no push token is sent to us. The app uses notifications only for this reminder; your alarms ring through Apple's alarm system, not through notifications. You can say no, or turn notifications off later in Settings; the app works the same either way.

## Ratings

The app may ask you to rate it using Apple's standard rating prompt. Apple handles the prompt and your rating; the app does not learn whether or how you rated it.

## When you email us

If you email us for support or a privacy request, we receive your email address, your name if your email includes it, your message and any attachments you choose to send, such as screenshots. Google processes this mail for us through Gmail. We use it only to answer and handle your request.

## Service providers

PostHog, RevenueCat and Google (Firebase Authentication, for sign-in, and Gmail, for email) process data for KLM Labs. We require the service providers that receive personal data from us to protect it at the same or an equivalent level as this policy describes and Apple's App Review Guidelines require. We do not sell personal data or share it for advertising.

## How long data is kept

Your alarms and settings stay on your device until you delete them in the app or delete the app; copies in your backups are managed separately.

We keep analytics events, crash reports, screen recordings, purchase records and support emails only as long as we need them to run, support and improve the app, or as the law requires (for example, purchase records for tax and accounting), and then delete them. Deleting the app does not delete records already sent to PostHog or RevenueCat; to ask us to delete them, see "Your choices and rights" below.

If you sign in, your account (email address, name, whether you used Apple or Google, and your sign-in dates) is kept in Firebase until you delete it or ask us to. A deleted account leaves Firebase at once, and our exported file the next time we export it; a file made before you deleted your account can hold your address until then. When you ask us by email, we delete the account and replace the file. Records already sent to PostHog and RevenueCat keep the random account ID, but once your account and that file are gone, nothing links it to your email address.

## Children

Flip Clock is a clock and alarm app and is not directed to children. We do not knowingly collect personal information from children. If you believe a child has used the app, contact us and we will delete any records we can find.

## Your choices and rights

- **Delete an alarm** in the app, or delete the app to remove everything it stored on your device.
- **Delete your account**, if you signed in: **Settings → Account → Delete my account** in the app, or email [klm.labs.inc@gmail.com](mailto:klm.labs.inc@gmail.com) and we will delete it (see "Signing in with Apple or Google").
- **Turn off alarm access or notifications** in Settings. Without alarm access, the app's alarms do not ring.
- **Cancel a subscription** in your Apple Account settings; see the [terms of use](/desk-clock/terms/). Deleting the app does not cancel it.
- **Ask us to delete analytics records (events, crash reports and recordings) or purchase records.** Email [klm.labs.inc@gmail.com](mailto:klm.labs.inc@gmail.com). Because these records use random identifiers, tell us roughly when you used the app and, for purchases, when you bought, so we can find them. If you signed in, the email address Settings shows helps us find them too. We will tell you what we could find and delete. Apple keeps its own purchase records.
- **Ask what we hold** by emailing the same address.

Depending on where you live, you may have further rights over personal data, such as access, correction, deletion and objection. Contact us and we will respond as the law requires.

## Changes to this policy

If the app's data practices change, we will update this policy and the App Store privacy details before that version is released. The effective date at the top shows the latest change. 2026-10-21: screen recordings, from version 1.0.1 (see "Product analytics"). 2026-11-02: optional sign-in with Apple or Google, and crash reports, from version 1.1.0 (see "Signing in with Apple or Google" and "Product analytics"). Questions: [klm.labs.inc@gmail.com](mailto:klm.labs.inc@gmail.com).
