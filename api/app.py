from flask import Flask, request
from flask_restful import Resource, Api
from core import money

app = Flask(__name__)
api = Api(app)

class MoneyApi(Resource):
    def get(self):
        # get the params
        try: 
            args = request.args
            value = args['value'] 
        except:
             return {'error': "expected param 'value' is not sent"},400          
        # validate the request
        validatedparam = money.formatMoney(value)
        if validatedparam == "":
            return {'error': 'server error, not able to parse the value'},400
        # return the parsed Value
        return {'parsedValue': validatedparam},201


api.add_resource(MoneyApi, '/money')

if __name__ == '__main__':
    app.run(debug=True)