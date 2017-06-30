from behave import *


@given('O usuario esta na pagina de login do sistema')
def open_site(context):
    context.browser.load_page("127.0.0.1:8000/login")
    context.browser.login('gianordolilucas@gmail.com','1q2w3e4r')


@when('O usuario digita senha atual "{old_password}" e "{password}" e "{confirm_password}"')
def change (context, old_password, password, confirm_password):
   context.browser.change_password_behave( old_password, password, confirm_password)


@then('O sistema informa "{notify_message_change}".')
def check_notify(context, notify_message_change):
    alert_value = context.browser.check_error_notify()
    form_value = context.browser.check_error_form()
    if alert_value is not None :
        assert notify_message_change in alert_value
    else:
        assert notify_message_change in form_value


