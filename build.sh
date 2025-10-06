#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

# Cria superusuário automaticamente
if [ "$CREATE_SUPERUSER" = "True" ]; then
  python manage.py createsuperuser \
    --email "$DJANGO_SUPERUSER_EMAIL" \
    --username "$DJANGO_SUPERUSER_USERNAME" \
    --no-input
fi