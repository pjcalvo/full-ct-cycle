#!/bin/bash
cd app
source venv/bin/activate
pip freeze
pytest --html=pytest-report/report.html