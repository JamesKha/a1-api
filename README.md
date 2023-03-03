# Quantum Software Engineering Bootcamp

## API Project - Assignment 1

### Getting started

Navigate to this project on a terminal window and create a virtual environment using Python:

```commandline
cd path/to/this/project
python3.11 -m venv .venv
source .venv/bin/activate
```

Install dev and app dependencies using Poetry ([follow this guide to install Poetry](https://python-poetry.org/docs/#installation)):

```commandline
poetry install
```

Or using pip:

```commandline
pip install -r requirements.txt
pip install -r dev-requirements.txt
```

#### Optional

Install and run pre-commit hooks. It's not necessary to install [pre-commit](https://pre-commit.com) as it's being installed as a dev dependency.

```commandline
pre-commit install
pre-commit run --all-files
```

### Run the app locally

Run the app using the command below; the app will be accessible at [http://127.0.0.1:8000](http://127.0.0.1:8000), and a Swagger UI will be accessible at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
The server will reload as files are updated.

```commandline
uvicorn app.main:app --reload
```

## Tests

Run tests:

```commandline
pytest
```
