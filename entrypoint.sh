#!/bin/bash
set -e

echo "waiting for database..."
while ! nc -z "${SQL_HOST:-db}" "${SQL_PORT:-5432}"; do
  sleep 0.5
done
echo "database available!"

python manage.py migrate --no-input
python manage.py collectstatic --no-input

exec gunicorn --bind 0.0.0.0:8000 --workers 3 config.wsgi:application