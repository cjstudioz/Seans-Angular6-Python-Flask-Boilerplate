FROM python:2.7-slim

RUN pip install gunicorn json-logging-py

#COPY logging.conf /logging.conf
#COPY gunicorn.conf /gunicorn.conf

COPY app.py /app.py
COPY routes /routes

EXPOSE 5000

ENTRYPOINT ["/usr/local/bin/gunicorn", "-b", ":5000", "app:app"]
