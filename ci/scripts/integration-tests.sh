#!/bin/bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

export FLASK_APP = "src/web/app.py"
export FLASK_RUN_PORT = "5000"


flask run

sleep 3

behave src/api/features/