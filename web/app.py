from flask import Flask, render_template, request
import requests
from dynaconf import settings as _settings

app = Flask(__name__)
api_url = "http://localhost:5000"

@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = ""
    if request.method == "POST":
        # try to format the money value
        try:
            value = request.form['money']
            r = requests.get(f"{api_url}/money?value={value}")
            results = r.json().get('parsedValue')
            print(results)
        except:
            errors.append(
                "Unable to get . Please make sure it's valid and try again."
            )
    return render_template('index.html', errors=errors, results=results)

if __name__ == '__main__':
      app.run(debug=True)