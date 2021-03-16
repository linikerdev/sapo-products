The goal of this project is to provide an API with products to use on a front end.

## Dependencies:
    - click
    - fastapi
    - h11
    - invoke
    - numpy
    - pandas
    - pydantic
    - python-dateutil
    - pytz
    - six
    - SQLAlchemy
    - starlette
    - typing-extensions
    - uvicorn

## Preconditions:

- Python 3
## Run local

### Install dependencies

```
pip install -r requirements.txt
```

### import the documents from type txt into the DataBase (repository).

```
invoke seed-db 
```
### Run server

```
python wsgy.py
```
## API documentation (provided by Swagger UI)

```
http://127.0.0.1:8000/docs

```

