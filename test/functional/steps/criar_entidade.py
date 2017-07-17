from behave import *

use_step_matcher("re")


@given("usuario entra no sistema e acessa o menu de cadastro de entidade")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass

@when('o usuario digitar "(?P<CPF_CNPJ>.+)", "(?P<NomeRazao>.+)", "(?P<NomeFantasia>.+)", e "(?P<Data_Nasc_Fund>.+)"')
def step_impl(context, CPF_CNPJ, NomeRazao, NomeFantasia, Data_Nasc_Fund):
    """
    :type context: behave.runner.Context
    :type CPF_CNPJ: str
    :type NomeRazao: str
    :type NomeFantasia: str
    :type Data_Nasc_Fund: str
    """
    pass


@then('O sistema tem como retorno a mensagem "(?P<mensagem>.+)"')
def step_impl(context, mensagem):
    """
    :type context: behave.runner.Context
    :type mensagem: str
    """
    pass