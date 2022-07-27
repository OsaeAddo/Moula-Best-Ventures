#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip
poetry install

python prod_manage.py collectstatic --no-input
python prod-manage.py makemigrations 
python prod-manage.py migrate
python prod-manage.py showmigrations