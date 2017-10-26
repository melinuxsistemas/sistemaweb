# Created by lucas at 14/07/2017
Feature: Entidade

  Scenario Outline: Cadastro nova entidade

    Given usuario entra no sistema e acessa o menu de cadastro de entidade e clica em adicionar entidade
    When  o usuario digitar "<cpf_cnpj>", "<entity_name>", "<fantasy_name>", "<birth_date_foundation>" e "<observation>"
    Then O sistema tem como retorno a mensagem "<mensagem>"
    Examples:sistema
      | cpf_cnpj  | entity_name | fantasy_name | birth_date_foundation | observation   |mensagem |
      |14960175796|Lucas Eduardo|Lucas         |04/04/1995             |texto teste    |  |
      |00000000000|Lucas Eduardo|Lucas         |04/04/1995             |texto teste    |cpf_cnpj: Cpf number is not valid. |
      |14960175796|Lucas Eduardo|Lucas         |04/04/1500             |texto teste    |  |
      |14960175796|Lucas Eduardo|Lucas         |04/04/3500             |texto teste    |  |

