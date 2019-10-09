from behave import given, when, then # pylint: disable=no-name-in-module
from src.api.features.page_model.money import Money

def money_instance(context):
    return Money(context)

@given('a "{}" as a test value')
def set_data(context,test_value):
    context.test_value = test_value
    # assert int(status) == 200, 
    # 

@when('I execute the request to format the money')
def execute_request(context):
    instance = money_instance(context)
    context.response = instance.formatMoney(context.test_value)

@then('the api will response "{}" code')
def check_response_code(context, reponse_code):
    print (context.response)
    assert int(context.response.status_code) == int(reponse_code), f"Actual status code '{context.response.status_code}', expected '{reponse_code}'"

@then('the expected value should be "{}"')
def check_response_value(context, response_value):
    result_value = context.response.json().get('parsedValue')
    assert result_value == response_value, f"Actual response value '{result_value}', expected '{response_value}'"