from behave import *


@given("O usuario esta no site do sistema e acessa registrar")
def open_site(context):
    context.browser.load_page("127.0.0.1:8000/login")


@when('O usuario informar email "{email}", "{password}" e "{confirm_password}"')
def autenticate_user(context,email,password,confirm_password):
    context.browser.temp['email'] = email
    context.browser.register(email,password,confirm_password)


@then('O sistema retorna "{notify_message_register}"')
def check_notify(context, notify_message_register):
    alert_value = context.browser.check_error_notify()
    print("VEJA O ALERTA: ",alert_value)

    if notify_message_register != 'OK':
        assert notify_message_register in alert_value

    else:
        assert alert_value is None

        context.browser.load_page(context.browser.project_url + 'api/user/register/delete/'+context.browser.temp['email']+'/')
        context.browser.temp = {}



