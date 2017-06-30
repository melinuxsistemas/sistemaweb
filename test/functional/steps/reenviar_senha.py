from behave import *


@given("O usuario precisa acessar /reset_password")
def open_site(context):
    context.browser.load_page("http://127.0.0.1:8000/reset_password/")


@when('O usuario digita seu email "{email}"')
def step_impl(context, email):
    context.browser.web_controller.enter_text('email', email)


@then('O Sistema notifica ao usuario "{notify_message}"')
def step_impl(context, notify_message):
    def check_notify(context, notify_message):
        alert_value = context.browser.check_error_notify()
        assert notify_message in alert_value