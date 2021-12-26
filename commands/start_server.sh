#!/bin/bash

python manage.py migrate
python manage.py collectstatic
python manage.py runserver_plus 0:"${WSGI_PORT}"