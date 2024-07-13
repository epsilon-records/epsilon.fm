<p align="center">
  <picture>
    <img src="https://github.com/epsilon-records/epsilon.fm/blob/0f0c8ecae0a27765dfece6c417c88b6068821e6e/src/lib/images/logo.png" width="130" alt="Logo for Epsilon">    
  </picture>
</p>

<h1 align="center">
  epsilon.FM
</h1>

<p align="center">
  A modern open-source music distribution platform.
</p>

<div align="center">

[![PRs-Welcome][contribute-image]][contribute-url]
[![Discord](https://img.shields.io/discord/412551291244380160?color=%235865F2&label=Discord&logo=discord&logoColor=%23fff)](https://discord.gg/NMKRYuzm)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fnatehouk%2Fepsilon.fm.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fnatehouk%2Fepsilon.fm?ref=badge_shield)

</div>

## Features

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

[contribute-url]: https://github.com/epsilon-records/epsilon.fm/blob/main/CONTRIBUTING.md
[contribute-image]: https://img.shields.io/badge/PRs-welcome-blue.svg
