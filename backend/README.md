# Backend - Manual Instructions

After completing the requirements outlined in the **📋 Prerequisites** section of the section on main [README.md](../README.md) project file, proceed with the following steps:

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/joaoflaviosantos/fastapi-async-sqlmodel-boilerplate.git
   ```

2. Navigate to the project directory:

   ```bash
   cd fastapi-async-sqlmodel-boilerplate/backend
   ```

3. Install dependencies using Poetry:

   ```bash
   poetry install
   ```

4. Define environment variables in ".env":

   - Copy the ".env.example" file as ".env":

     ```bash
     cp .env.example .env
     ```

   - Open the ".env" file and modify the environment variables accordingly.

     **Note:** Make sure to set a secure and unique value for the `SECRET_KEY`.

     You can generate a secure secret key using the following command:

     ```bash
     poetry run python -c "from fastapi import FastAPI; import secrets; print(secrets.token_urlsafe(32))"
     ```

## 🔀 Database Migration

To create tables in the database, run Alembic migrations:

```bash
poetry run alembic revision --autogenerate
```

And to apply the migration:

```bash
poetry run alembic upgrade head
```

For detailed instructions on database migration using Alembic, refer to the [Database Migrations Guide](../docs/database-migration-guide.md) in the project's documentation.

## 🚀 Running the Backend

Start the FastAPI application:

```bash
poetry run uvicorn src.main:app --reload
```

For more details on running the backend with Uvicorn, consult the [Uvicorn Guide](../docs/uvicorn-guide.md) in the project's documentation.

Start the ARQ worker:

```bash
poetry run arq src.worker.WorkerSettings
```

For more details on running the ARQ worker, refer to the [ARQ Guide](../docs/arq-guide.md) in the project's documentation.

## 🧪 Running Tests

Run tests using pytest:

```bash
poetry run python -m pytest -vv ./tests
```

For detailed guidance on running tests and confirming the application's behavior, refer to the [Testing Guide](../docs/testing-guide.md) in the project's documentation.

## 🚧 Pre-Commit Instructions

Before committing changes, ensure that you've activated the virtual environment in 'backend/.venv' at the root of the project. This step is crucial for the successful execution of pre-commit hooks. Activate the virtual environment using the following command in the root folder of your project:

```bash
source backend/.venv/bin/activate
```

After activating the virtual environment, pre-commit hooks will check your commits before they are committed.

Explore comprehensive instructions for setting up pre-commit steps and understanding their benefits in the [Pre-Commit Guide](../docs/pre-commit-instructions.md) located within the project's documentation.
