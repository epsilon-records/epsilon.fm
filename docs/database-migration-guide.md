# Database Migration with Alembic

## What is Alembic?

[Alembic](https://alembic.sqlalchemy.org/) is a database migration tool for SQLAlchemy, a popular Python library for interacting with relational databases. In simple terms, database migrations are scripts that describe changes to the database structure over time.

## Why are Migrations Necessary?

- **Schema Evolution:** As your application evolves, it's common for the database structure to evolve as well. New tables may be added, columns modified or removed, etc.

- **Consistency Across Environments:** Migrations ensure that all environments (development, testing, production) have the same database structure, avoiding inconsistencies and errors related to schema differences.

- **Database Versioning:** Alembic provides a versioning system for the database, allowing you to track applied changes and revert or advance to specific versions as needed.

## How to Execute Migrations with Alembic

1. **Auto-generating Revisions:**

   - When starting a new feature or making changes to the data model, you can use the command `poetry run alembic revision --autogenerate` to auto-generate a new revision. This creates a new migration script based on changes detected in the data model.

2. **Applying Migrations:**

   - After auto-generating a revision, you can apply it to the database using the command `poetry run alembic upgrade head`. This effectively applies all pending migrations.

3. **Reverting Migrations (Optional):**
   - If necessary, you can revert to a previous version of the database using `poetry run alembic downgrade -1` to revert a specific migration or `poetry run alembic downgrade base` to revert all migrations.

## Why Users Should Execute Migrations

- **Maintain Consistency:** Running migrations ensures that the database is up-to-date with the latest version of the data model, maintaining consistency across different environments and avoiding compatibility issues.

- **Tracking Changes:** Using migrations allows you to track and manage changes to the database over time. This is crucial for maintaining a clear history of modifications.

- **Ensure Proper Operation:** Some changes to the data model may be essential for the proper operation of the application. Running migrations ensures that the database is configured as expected.

**Note:** Ensure these commands are executed within the 'backend' folder of your project.

Encourage users to run migrations whenever there are significant changes to the data model to ensure a cohesive and functional database environment.

---

[Back to backend README](../backend/README.md)
