from test.functional.config.web_controller import DjangoWebTest


def before_all(context):
    context.browser = DjangoWebTest()

def after_all(context):

    context.browser.close()



