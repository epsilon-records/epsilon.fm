# Pre-Commit: Instructions and Benefits

## Why Pre-Commit?

Pre-commit steps are a crucial part of the development process, designed to ensure consistency, quality, and integrity of the source code before being committed to the repository. They bring significant benefits to developers and the project as a whole.

## Benefits

### 1. Code Consistency

Pre-commit hooks help maintain a consistent code style throughout the project. This makes the code more readable for other developers and aids in long-term maintenance.

### 2. Early Issue Identification

Running automated tests, linting, and other checks before committing allows for early identification of issues, reducing the likelihood of errors in the code and improving overall software quality.

### 3. Commit Message Standardization

Enforcing standards for commit messages ensures clear and consistent documentation of the change history, making code review and collaboration among developers more straightforward.

## Usage Instructions

Before committing your changes to the repository, follow the steps below:

1. Activate the virtual environment in the 'backend' directory (when in the root directory):

   ```bash
   source backend/.venv/bin/activate
   ```

2. Ensure you are in the root directory of the project.

3. Execute the following command to ensure that pre-commit hooks are applied:

   ```bash
   pre-commit run --all-files
   ```

   This will automatically check and fix identified issues in modified files.

4. After successful execution, you can proceed to commit your changes as usual.

By following these instructions, you ensure a smoother workflow and contribute to the overall code quality in the project.

---

[Back to backend README](../backend/README.md)
