from behave import *

use_step_matcher("re")


@given("usuario entra no sistema e acessa o menu de cadastro de entidade e clica em adicionar entidade")
def step_impl(context):
    context.browser.load_page("127.0.0.1:8000/login")
    context.browser.login('gianordolilucas@gmail.com','1q2w3e4r')



@when(
    'o usuario digitar "(?P<cpf_cnpj>.+)", "(?P<entity_name>.+)", "(?P<fantasy_name>.+)", "(?P<birth_date_foundation>.+)" e "(?P<observation>.+)"')
def step_impl(context, cpf_cnpj, entity_name, fantasy_name, birth_date_foundation, observation):
   context.browser.add_entity(cpf_cnpj,entity_name,fantasy_name,birth_date_foundation,observation)



@then('O sistema tem como retorno a mensagem "(?P<mensagem>.+)"')
def step_impl(context, mensagem):
    """
    :type context: behave.runner.Context
    :type mensagem: str
    """
    pass