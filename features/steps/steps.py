from behave import given, when, then
from features.browser import Browser
from test.functional.selenium_controller.web_controller import *

@given('a user visits the site')
def given_visit (context):
    browser = Browser()
    browser.visit('login')

@when('I log in as "uservalid"')
def tentar_logar(context):
    browser = Browser()
    browser.tryLogg('gianordolilucas@gmail.com', '1q2w3e4r')

@when('I log in as "userinvalid"')
def tentar_logar(context):
    browser = Browser()
    browser.tryLogg('invalido@','1q2w3e')

@then('I see "{Sistemaweb - Base Page}"')
def step_impl(context, arg0):
    """
    :type context: behave.runner.Context
    :type arg0: str
    """
    pass