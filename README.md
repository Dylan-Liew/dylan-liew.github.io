# x44ylan

A personal landing page at [x44ylan.com](https://x44ylan.com/), built with VitePress and a Three.js mountain scene. Social icons sit below the name, with a theme switch in the corner and GitHub light and dark colours.

## Development

Use Node 22 or later.

```sh
npm ci
npm run dev
```

## Build and preview

```sh
npm run build
npm run preview -- --host 127.0.0.1
```

The landing page lives in `docs/index.md`. Its components and styles live in `docs/.vitepress/theme`. The mountain is static. It renders on load, theme changes, resize, and graphics-context recovery, with no animation loop or cursor movement. It falls back to a static background when WebGL is unavailable.

## Browser verification

Open the preview with Playwright CLI and run the landing-page check:

```sh
mkdir -p /tmp/landing-check
playwright-cli -s=landing open http://127.0.0.1:4173/
playwright-cli -s=landing run-code --filename=scripts/check-site.js
playwright-cli -s=landing run-code --filename=scripts/check-mobile.js
```

The checks cover desktop and phone layouts, social links, theme switching, the static scene lifecycle, WebGL fallback, and removal of study pages. The mobile check uses touch input and verifies that the mountains stay still without ongoing rendering. Screenshots are saved to `/tmp/landing-check`.

## Deployment

Pushing `main` builds the landing page and deploys it to GitHub Pages. Study notes are maintained separately in Docs.
