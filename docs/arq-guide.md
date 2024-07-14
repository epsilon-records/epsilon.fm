# ARQ Guide

## Overview

ARQ is a high-performance Python library for handling background tasks, designed to be compatible with ASGI frameworks like FastAPI. This guide provides instructions on how to start the ARQ worker and leverage its features within the project.

## Introduction to ARQ

[ARQ](https://arq-docs.helpmanual.io/) is a background task library for Python that integrates seamlessly with FastAPI and other ASGI frameworks. It is built with performance in mind, allowing you to handle background tasks efficiently and asynchronously.

### Key Features

- **Efficient Task Queue Management:** ARQ simplifies the handling of background tasks, making it easy to manage and execute tasks asynchronously.

- **ASGI Compatibility:** ARQ is designed to work seamlessly with ASGI frameworks like FastAPI, providing a smooth integration for background task processing.

## Running the ARQ Worker

To start the ARQ worker, follow these steps:

```bash
poetry run arq src.worker.WorkerSettings
```

This command launches the ARQ worker, allowing for efficient background task queue management.

For more details and advanced configuration options when running the ARQ worker, refer to the [ARQ Documentation](https://arq-docs.helpmanual.io/).

---

[Back to backend README](../backend/README.md)
