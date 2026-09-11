# Standing rules

- Policy text must match the app repo’s `docs/store/privacy-policy.md`, actual
  behavior, and current Play/Apple store declarations. Check `lib/analytics.ts`
  and `app.config.ts` before publishing. If source prose is stale, publish the
  code-correct explanation and record exact differences for the app team.
- Never break or redirect away a registered privacy, terms or support URL.
  Existing routes must retain their paths and return 200.
- Never fabricate ratings, stars, reviews, download counts, awards or testimonials.
- Use the shared generator, templates and assets. Adding an app means data,
  actual screenshots, app icons and reviewed policy text, not copied HTML.
- Keep site actions and focus ink-led. Red is reserved for errors; do not repaint
  the app’s real captures or original icon to fit the website.
- Treat `/work/apps/invoice-creator` as read-only. Never edit, install, commit or
  check out anything there. Keep secrets and all `~/.config` files out of this repo.
- Check source and built output, inspect mobile/desktop renders, and **verify live
  after every push**: matching Pages build SHA, HTTP 200 routes, current policy text
  and working assets. Follow the README for store states and publishing checks.
