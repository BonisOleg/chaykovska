#!/usr/bin/env bash
# Виходимо з помилкою у разі фейлу
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
