from flask import Flask, render_template, request
import requests

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
            float(value)
            r = requests.get(f"{api_url}/money?value={value}")
            results = r.json().get('parsedValue')
            print(results)
        except ValueError:
            errors.append("Unable to process the request. Please make sure the number is valid.")
        except:
            errors.append("Unable to process the request. Please try again later.")
    return render_template('index.html', errors=errors, results=results)

if __name__ == '__main__':
      app.run(debug=True)