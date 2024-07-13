# epsilon.fm

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fnatehouk%2Fepsilon.fm.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fnatehouk%2Fepsilon.fm?ref=badge_shield)

Our modern open-source platform includes features like an artist website, social media management, and merch, empowering you with global reach and full control over your creative work.

## Developing

Once you've cloned the code and installed dependencies with `bun install`, you can start the development server as follows:

```bash
bun run dev

# or start the server and open the app in a new browser tab
bun run dev -- --open
```

## Building

To create a production version of the app:

```bash
bun run build
```

You can preview the production build with `bun run preview`.

## Todo

```
[x] Bootstrap frontend (sveltekit)
[x] Deploy frontend via cicd (vercel)
[x] Implement authentication (clerk)
[x] Implement error handling (sentry)
[x] Implement analytics (posthog, vercel, meticulous.ai)
[x] Implement file uploads (uploadthing)
[ ] Implement release form
[ ] Implement track form
[x] Implement artist websites
[ ] Implement wildcard domains
[x] Implement mobile and desktop applications (tauri)
[x] Bootstrap backend api (fastapi, sqlmodel)
[x] Deploy backend via cicd (digitalocean)
[ ] Implement backend api
[ ] Remove server side rendering by switching to backend api (required for tauri)
```

## License

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fnatehouk%2Fepsilon.fm.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fnatehouk%2Fepsilon.fm?ref=badge_large)
