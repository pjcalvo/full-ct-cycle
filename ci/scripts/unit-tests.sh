#!/bin/bash
ls venv
. venv/bin/activate
pytest --html=pytest-report/report.html