#!/bin/bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

FLASK_APP = src/web/app.py
FLASK_RUN_PORT = 5001

cd app
source venv/bin/activate
flask run

sleep 3

behave src/api/features/