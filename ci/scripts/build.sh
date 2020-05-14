#!/bin/bash
FLASK_APP = src/web/app.py
FLASK_RUN_PORT = 5001

cd app
source venv/bin/activate
flask run