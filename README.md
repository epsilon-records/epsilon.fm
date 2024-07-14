<h1 align="center">
  epsilon.FM
</h1>

<p align="center" markdown=1>
  A modern open-source music distribution platform.
</p>

<p align="center">
  <picture>
    <img src="https://github.com/epsilon-records/epsilon.fm/blob/0f0c8ecae0a27765dfece6c417c88b6068821e6e/src/lib/images/logo.png" width="130" alt="Logo for Epsilon">    
  </picture>
</p>

<p align="center">
  <a href="https://www.python.org">
      <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://fastapi.tiangolo.com">
      <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI">
  </a>
  <a href="https://sqlmodel.tiangolo.com">
      <img src="https://img.shields.io/badge/SQLModel-7E56C2?style=for-the-badge&logo=sqlmodel&logoColor=fff" alt="SQLModel">
  </a>
  <a href="https://docs.pydantic.dev/2.4/">
      <img src="https://img.shields.io/badge/Pydantic-E92063?logo=pydantic&logoColor=fff&style=for-the-badge" alt="Pydantic">
  </a>
  <a href="https://docs.sqlalchemy.org/en/20/">
      <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=fff" alt="SQLAlchemy">
  </a>
  <a href="https://www.postgresql.org">
      <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  </a>
  <a href="https://redis.io">
      <img src="https://img.shields.io/badge/Redis-DC382D?logo=redis&logoColor=fff&style=for-the-badge" alt="Redis">
  </a>
  <a href="https://docs.docker.com/compose/">
      <img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff&style=for-the-badge" alt="Docker">
  </a>
  <a href="https://nginx.org/en/">
      <img src="https://img.shields.io/badge/NGINX-009639?logo=nginx&logoColor=fff&style=for-the-badge" alt=NGINX>
  </a>
</p>

<div align="center">

[![PRs-Welcome][contribute-image]][contribute-url]
[![Discord](https://img.shields.io/discord/412551291244380160?color=%235865F2&label=Discord&logo=discord&logoColor=%23fff)](https://discord.gg/NMKRYuzm)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fnatehouk%2Fepsilon.fm.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fnatehouk%2Fepsilon.fm?ref=badge_shield)

</div>

# 🔍 Project Overview

This **SvelteKit** powered open-source music distribution platform aims to revolutionize how independent artists share and monetize their music. Built with modern web technologies and a focus on user experience, our platform provides a comprehensive suite of tools for artists to manage their releases, engage with fans, and track their success.

Key features include:

- **Music Distribution**: Seamless uploading and distribution of tracks to major streaming platforms.
- **Artist Profiles**: Customizable artist pages to showcase music, biography, and upcoming events.
- **Release Management**: Tools for creating and managing music releases, including metadata editing and scheduling.
- **Analytics Dashboard**: Real-time streaming and revenue data to help artists track their performance.
- **Social Media Integration**: Easy sharing of releases and updates across various social platforms.
- **Royalty Tracking**: Transparent royalty calculations and payout management.

The project leverages the power of **SvelteKit** for a blazing-fast frontend, **Drizzle ORM** for efficient database operations, and integrates with services like **Clerk** for authentication and **UploadThing** for file handling. The modular structure allows for easy expansion and customization.

Key areas of the platform include:

- `routes/(main)`: Core pages like homepage, artist dashboard, and release management.
- `routes/(website)`: Artist-specific public-facing pages.
- `lib/components`: Reusable UI components for consistent design.
- `lib/db`: Database schema and operations using Drizzle ORM.
- `lib/server`: Server-side utilities and integrations.

This project aims to provide a **robust and scalable solution** for music distribution while remaining open-source and community-driven. It serves as an excellent foundation for music tech enthusiasts, independent labels, and developers looking to contribute to the music industry's digital transformation.

Our goal is to empower artists with a platform that combines ease of use with powerful features, all while fostering an open ecosystem for music distribution technology.

## 🌟 Key Features

This project aims to provide a **robust open-source platform for music distribution**, incorporating modern web technologies and user-centric design:

- 🎵 **Music Distribution:** Seamlessly upload and distribute tracks to major streaming platforms.
- 👤 **Artist Profiles:** Create customizable artist pages to showcase music, biography, and events.
- 📅 **Release Management:** Comprehensive tools for creating, editing, and scheduling music releases.
- 📊 **Analytics Dashboard:** Real-time streaming and revenue data for performance tracking.
- 🌐 **Social Media Integration:** Easy sharing of releases and updates across various platforms.
- 💰 **Royalty Tracking:** Transparent calculations and management of royalty payouts.
- ⚡ **SvelteKit Powered:** Utilize SvelteKit for a blazing-fast, reactive user interface.
- 🗃️ **Drizzle ORM:** Efficient database operations with type-safe queries.
- 🔐 **Clerk Authentication:** Secure and customizable user authentication and management.
- 🗂️ **UploadThing Integration:** Robust file handling for music and image uploads.
- 🎨 **Customizable UI Components:** Reusable components for consistent design across the platform.
- 📱 **Responsive Design:** Mobile-friendly interface for on-the-go management.
- 🔍 **SEO Optimization:** Built-in features to improve discoverability of artist pages.
- 🌍 **Internationalization:** Support for multiple languages to reach a global audience.
- 🚀 **Scalable Architecture:** Designed to handle growth from indie artists to major labels.
- 🧩 **Modular Structure:** Easy to extend and customize for specific needs.
- 🐳 **Docker Support:** Simplified deployment and development environments.
- 👥 **Open-Source Community:** Benefit from and contribute to a growing ecosystem of music tech.

## 📋 Prerequisites

Before you begin, ensure you have the following prerequisites installed and configured:

- [PostgreSQL](https://www.postgresql.org): Set up a PostgreSQL database.
- [Redis](https://redis.io): Install and configure a Redis server.
- [Python](https://www.python.org): Make sure to have Python 3.11 or a newer version installed on your system.
- [Poetry](https://python-poetry.org): Install Poetry for managing dependencies.

**Note:** Soon, there will be an additional option for development using Docker containers.

# Frontend

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

# Backend

## Installing Poetry

Poetry is a dependency manager for Python. Follow the steps below to install Poetry:

1. Open a terminal.

2. Run the following command to install Poetry using pip:

   ```bash
   pip install poetry
   ```

3. Verify the installation by running:

   ```bash
   poetry --version
   ```

   This should display the installed Poetry version.

Now that the requirements are met, you can begin working on your project. For more details for a manual setup, please refer to the [Backend README](backend/README.md) section.

## Todo

```
[x] Bootstrap frontend (SvelteKit)
[x] Deploy frontend via CICD (Vercel)
[x] Implement authentication (Clerk)
[x] Implement error handling (Sentry)
[x] Implement analytics (Posthog, Vercel)
[x] Implement testing (Checkly, Meticulous)
[x] Implement file uploads (UploadThing)
[ ] Implement release form
[ ] Implement track form
[x] Implement artist websites
[ ] Implement wildcard domains
[x] Implement mobile and desktop applications (Tauri)
[x] Bootstrap backend API (FastAPI, SQLModel)
[x] Deploy backend via CICD (DigitalOcean)
[ ] Implement backend API
[ ] Remove server side rendering by switching to backend api (required for tauri)
```

## License

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fnatehouk%2Fepsilon.fm.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fnatehouk%2Fepsilon.fm?ref=badge_large)

[contribute-url]: https://github.com/epsilon-records/epsilon.fm/blob/main/CONTRIBUTING.md
[contribute-image]: https://img.shields.io/badge/PRs-welcome-blue.svg

## 🎯 Project Goals

- [x] Leverage the power of FastAPI for building high-performance APIs.
- [x] Implement asynchronous programming wherever applicable for optimal performance.
- [x] Integrate Redis for caching, rate limiting, and improving data access speed.
- [x] Utilize ARQ for handling background tasks asynchronously.
- [x] Implement a robust logging system to track and manage application events efficiently.
- [x] Manage database migrations seamlessly using Alembic.
- [x] Develop comprehensive unit tests for API endpoints using pytest.
- [x] Implement using SQLModel to streamline the interaction between the database and the API.
- [ ] Provide a CLI tool for easy project execution and management.
- [ ] Provide diverse deployment options to ensure flexibility and accessibility.


