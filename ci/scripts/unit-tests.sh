#!/bin/bash
cd app
source venv/bin/activate
pytest --html=pytest-report/report.html