release: cd app && python3 manage.py migrate && python3 manage.py crontab add .
web: sh -c 'cd ./app/ && gunicorn app.wsgi' --preload --log-file –