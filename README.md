# Top Music Brazil

Web Scrapping and API for query into 100 songs most listened in Brazil, made with Python.

## Requirements

* Python > `3.10`
* PIP
* Linux (optional)

## Instalation

Init virtual enviroment.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependences.

```bash
pip install -r requirements.txt
```

## Running

### Web scrapping

### REST API

```bash
uvicorn sql_app.main:app --reload
```

#### Routes
