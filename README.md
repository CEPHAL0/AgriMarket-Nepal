# Branch Naming

`username/branchPurpose`

Eg:
`sharad/AddMigrationFiles`


## Scripts:

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

Run backed
```shell
uvicorn main:app --host <host> --port <portnumber> --reload
```

**Postgresql url format:**`DATABASE_URI = 'postgresql://postgres:<password>@localhost/<name_of_the_datbase>'`