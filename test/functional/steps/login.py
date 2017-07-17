from behave import given, when, then


@given('O usuario esta no site do sistema')
def open_site(context):
    context.browser.load_page("127.0.0.1:8000/profile")


@when('O usuario informar"{email}" e "{password}"')
def autenticate_user(context,email,password):
    context.browser.login(email,password)


@then('O sistema notifica "{notify_message}"')
def check_notify(context, notify_message):
    alert_value = context.browser.check_error_notify()
    assert notify_message in alert_value

