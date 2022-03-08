FROM python:3.8.10

RUN apt update
RUN alias py=python

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /django-crontab

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . /django-crontab/

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000