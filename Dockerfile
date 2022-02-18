FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN python3 django/manage.py makemigrations
RUN python3 django/manage.py migrate