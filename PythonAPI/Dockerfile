FROM python:2.7-slim

RUN pip install flask
RUN pip install Flask-Cors
RUN pip install gunicorn

COPY PythonAPI/app.py /app.py
COPY PythonAPI/routes /routes

EXPOSE 5000

#ENTRYPOINT ["/usr/local/bin/gunicorn", "-b", ":5000", "app:app"]
