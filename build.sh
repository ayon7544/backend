#!/bin/bash
set -o errexit  # Stop script execution on error

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Migrate database
python manage.py migrate

# Create superuser if specified
if [[ $CREATE_SUPERUSER ]]; then
    python manage.py createsuperuser --noinput --email "$DJANGO_SUPERUSER_EMAIL" --username "$DJANGO_SUPERUSER_USERNAME"
fi
