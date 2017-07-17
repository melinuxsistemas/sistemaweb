# Created by lucas at 14/07/2017
Feature: Entidade

  Scenario Outline: Cadastro nova entidade

    Given usuario entra no sistema e acessa o menu de cadastro de entidade
    When  o usuario digitar "<CPF_CNPJ>", "<NomeRazao>", "<NomeFantasia>", e "<Data_Nasc_Fund>"
    Then O sistema tem como retorno a mensagem "<mensagem>"
    Examples:sistema
      | CPF_CNPJ | NomeRazao | NomeFantasia | Data_Nasc_Fund | mensagem |
