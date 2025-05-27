#!/bin/bash

# Run migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Seed Database
python3 manage.py loaddata superusers.json
python3 manage.py loaddata lock_types.json

# Collect static files
python manage.py collectstatic --noinput

# Run the specified command (if any)
exec "$@"