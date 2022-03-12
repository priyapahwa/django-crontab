FROM python:3.8.10

RUN apt update
RUN alias py=python
RUN apt-get install cron -y

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /django-crontab

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . /django-crontab/

# django-crontab logfile
RUN mkdir /cron
RUN touch /cron/django_cron.log

EXPOSE 8000

CMD service cron start && python manage.py runserver 0.0.0.0:8000