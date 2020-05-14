#!/bin/bash
ls
cd app
ls
source venv/bin/activate
pytest --html=pytest-report/report.html