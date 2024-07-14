# Uvicorn Guide

## Overview

Running the FastAPI application asynchronously is made possible with Uvicorn. Uvicorn is an ASGI (Asynchronous Server Gateway Interface) server that provides a fast and efficient way to serve FastAPI applications.

## Introduction to Uvicorn

[Uvicorn](https://www.uvicorn.org/) is a lightweight ASGI server that allows FastAPI applications to take full advantage of asynchronous programming. It is designed to deliver high performance and is particularly well-suited for applications with high concurrency.

### Key Features

- **Asynchronous Support:** Uvicorn fully supports asynchronous programming, allowing FastAPI to handle many requests concurrently without blocking.

- **Automatic Reloading:** The `--reload` option, as used in the command below, enables automatic reloading of the server during development, making the development process smoother.

## Running the Backend with Uvicorn

To start the FastAPI application asynchronously using Uvicorn, follow these steps:

```bash
poetry run uvicorn src.main:app --reload
```

This command launches the FastAPI application, enabling asynchronous functionality with automatic reloading during development.

For more details and advanced configuration options when running the backend with Uvicorn, refer to the [Uvicorn Documentation](https://www.uvicorn.org/).

---

[Back to backend README](../backend/README.md)
