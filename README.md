# Top Music Brazil

Web Scrapping and API for query into 100 songs most listened in Brazil, made with Python.

## Requirements

* Python > `3.10`
* PIP
* Linux (optional)

## Tech stack

* Web Scrapping: Python + requests + BeautifulSoap
* REST API: Python + FastAPI
* Database: SQLite + SQLAlchemy

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

First, run the scrapping, then run the REST API.

### Web scrapping

```bash
python feed_app/main.py
```

### REST API

```bash
uvicorn sql_app.main:app --reload
```

#### Routes

List all songs: `GET /songs`

```
curl http://localhost:8000/songs
```
