# Wagtail Purge

A simple admin UI for removing individual pages from your CDN's cache. Assumes that your Wagtail site has already been configured with [frontend cache invalidation](https://docs.wagtail.io/en/stable/reference/contrib/frontendcache.html).

## Instructions

1. Install this app with `pip install wagtail-purge`
2. Add `"wagtail_purge"` to your `INSTALLED_APPS`
3. Visit 'CDN purge' in your admin settings menu