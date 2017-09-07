# Created by lucas at 14/07/2017
Feature: Entidade

  Scenario Outline: Cadastro nova entidade

    Given usuario entra no sistema e acessa o menu de cadastro de entidade
    When  o usuario digitar "<cpf_cnpj>", "<nome_razao>", "<nome_fantasia>", e "<nascimento_fundacao>"
    Then O sistema tem como retorno a mensagem "<mensagem>"
    Examples:sistema
      | cpf_cnpj | nome_razao | nome_fantasia | nascimento_fundacao | mensagem |
