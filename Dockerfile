FROM python:3.10.13-slim-bullseye
COPY . /top-music-br
WORKDIR /top-music-br
# Install dependences.
RUN pip install -r requirements.txt
# First, run the scrapping
RUN python feed_app/main.py
# Expose port
EXPOSE 8000
# Then run the REST API
CMD [ "uvicorn", "sql_app.main:app", "--host", "0.0.0.0", "--port", "8000" ]
