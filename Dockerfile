FROM python:3.8
WORKDIR /app
COPY . /app
RUN apt-get update && \
    apt-get install gettext -y
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
RUN python manage.py compilemessages
CMD uwsgi --module=spacescoop.wsgi --http=0.0.0.0:80
