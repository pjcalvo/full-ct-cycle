from behave import given, when, then # pylint: disable=no-name-in-module
from src.api.features.page_model.api_base import ApiBase

@given('As a user of the application')
def step_impl(context):
    context.api_instance = ApiBase(context)