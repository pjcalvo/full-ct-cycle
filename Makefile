app:
	FLASK_APP=src/api/app.py flask run

app-web:
	FLASK_RUN_PORT=5001 FLASK_APP=src/web/app.py flask run

test-unit:
	pytest --html=pytest-report/report.html

test-api:
	behave src/api/features/

test-e2e:
	npm run test