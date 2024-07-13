<p align="center">
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/t3-oss/create-t3-app/99286f37324330ecdf75132fae1f246440a88035/www/public/images/t3-light.svg">
  <img src="https://raw.githubusercontent.com/t3-oss/create-t3-app/99286f37324330ecdf75132fae1f246440a88035/www/public/images/t3-dark.svg" width="130" alt="Logo for T3">
</picture>
</p>

<h1 align="center">
  create-t3-app
</h1>

<p align="center">
  Interactive CLI to start a full-stack, typesafe Next.js app.
</p>

<p align="center">
  Get started with the <a rel="noopener noreferrer" target="_blank" href="https://init.tips">T3 Stack</a> by running <code>npm create t3-app@latest</code>
</p>

<div align="center">

[![PRs-Welcome][contribute-image]][contribute-url] [![Discord](https://img.shields.io/discord/966627436387266600?color=%235865F2&label=Discord&logo=discord&logoColor=%23fff)](https://t3.gg/discord) [![NPM version][npm-image]][npm-url]
[![Downloads][downloads-image]][npm-url]

</div>

<a href="http://www.youtube.com/watch?v=PbjHxIuHduU" target="_blank">
  <p align="center">
    <img src="https://t3.gg/random/T3%20Stack%20V4.png" alt="Video thumbnail of Theo with an indecipherable expression on his face" width="320" />
  </p>
</a>

<a href="http://www.youtube.com/watch?v=PbjHxIuHduU" target="_blank">
  <p align="center">Watch Theo's overview on Youtube here</p>
</a>

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

[downloads-image]: https://img.shields.io/npm/dm/create-t3-app?color=364fc7&logoColor=364fc7
[npm-url]: https://www.npmjs.com/package/create-t3-app
[npm-image]: https://img.shields.io/npm/v/create-t3-app?color=0b7285&logoColor=0b7285
[contribute-url]: https://github.com/t3-oss/create-t3-app/blob/main/CONTRIBUTING.md
[contribute-image]: https://img.shields.io/badge/PRs-welcome-blue.svg
