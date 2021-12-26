#!/bin/bash

python manage.py migrate
python manage.py collectstatic
python manage.py runserver_plus --cert-file cert.pem --key-file key.pem 0:"${WSGI_PORT}"