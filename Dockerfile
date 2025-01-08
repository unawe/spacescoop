FROM python:3.10

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt /app/

RUN apt-get update && \
    apt-get install gettext python3-cffi libcairo2 libpango-1.0-0 \
    libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info \
    postgresql-client libpq-dev postgresql-contrib -y && \
    pip install -r requirements.txt

COPY . /app/

RUN python manage.py migrate && \
    python manage.py compilemessages && \
    python manage.py collectstatic --noinput

EXPOSE 80

CMD ["gunicorn", "spacescoop.wsgi:application", "--bind", "0.0.0.0:80"]
