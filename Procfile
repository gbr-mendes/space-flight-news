release: cd app && python3 manage.py migrate
web: gunicorn app/app.wsgi --preload --log-file –