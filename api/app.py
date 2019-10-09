from flask import Flask, request, abort
from flask_restful import Resource, Api
from core import money
import logging

logging.basicConfig(filename='logging.log',level=logging.DEBUG)

app = Flask(__name__)
api = Api(app)

class MoneyApi(Resource):
    def get(self):            
        value = request.args.get('value', 1, type=float)     
        validatedparam = money.formatMoney(value)
        if validatedparam == "":
            logging.error('server error, not able to parse the value')
            abort(400) 
        # return the parsed Value
        logging.info(f'Original value: {value} . Formatted value: {validatedparam}')
        return {'parsedValue': validatedparam},201

class Main(Resource):
    def get(self):
        return {'status': 'site is up and running'},201

api.add_resource(MoneyApi, '/money')
api.add_resource(Main, '/')

if __name__ == '__main__':
    app.run(debug=True)