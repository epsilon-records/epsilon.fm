# Testing Guide

## Overview

Testing is a crucial aspect of software development, ensuring that the application functions as intended and that new changes do not introduce regressions. This guide provides instructions on how users can run tests to verify the correct functionality of the application.

## Running Tests

To run tests for the project, follow these steps:

1. Navigate to the 'backend' directory:

   ```bash
   cd backend
   ```

2. Execute the following command to run tests:

   ```bash
   poetry run python -m pytest -vv ../tests -s
   ```

   This command runs the tests located in the 'tests' directory with detailed output.

3. Review the test results in the terminal. Any failures or errors will be highlighted.

## Writing Tests

If you want to contribute or extend the test coverage, consider the following:

- Tests are located in the 'tests' directory, organized by the structure of the 'src' directory.

- Use the [pytest](https://docs.pytest.org/en/stable/) testing framework for writing tests.

- Aim to cover different aspects of your application, including unit tests, integration tests, and any other relevant scenarios.

## Continuous Integration

The project may be set up with continuous integration (CI) tools that automatically run tests upon each commit. Be sure to check the CI status for the latest test results.

By following these testing practices, you contribute to the reliability and stability of the project.

---

[Back to backend README](../backend/README.md)
