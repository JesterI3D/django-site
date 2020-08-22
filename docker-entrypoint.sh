#!/usr/bin/env bash

python manage.py migrate                  # Apply database migrations
python manage.py collectstatic --noinput  # Collect static files

# Prepare log files and start outputting logs to stdout
#tail -n 0 -f /srv/logs/*.log &

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn mysite.wsgi:application/
    --bind 0.0.0.0:8000/
    --debug --log-level debug/
    "$@"
