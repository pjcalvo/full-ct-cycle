#!/bin/bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt


FLASK_APP=src/web/app.py FLASK_RUN_PORT=5000 flask run

sleep 3

behave src/api/features/