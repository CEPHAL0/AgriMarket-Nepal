# Branch Naming

`username/branchPurpose`

Eg:
`sharad/AddMigrationFiles`

## Scripts

Activate venv

```shell
source venv/Srcipts/activate
```

Add Requirements to requirements.txt

```shell
pip freeze>requirements.txt
```

Generate Migration Files automatically

```shell
alembic revision --autogenerate  -m "<migration_file_name>"
```

Run migrations

```shell
alembic upgrade head
```

Run backed

```shell
uvicorn main:app --host <host> --port <portnumber> --reload
```

Remove all of the `__pycache__` folders

```shell
find -type d -name __pycache__ -exec rm -rf {} +
```

## Migration Guide

Run the following commands initially

```shell
alembic revision --autogenerate -m "Inital Setup"
```

### *Before doing some changes, you can delete the alembic_versions and other tables before generating migration files again*

**Postgresql url format:**`DATABASE_URI = 'postgresql://postgres:<password>@localhost/<name_of_the_datbase>'`
