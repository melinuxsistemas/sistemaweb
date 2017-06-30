Feature: Login

  Scenario Outline: O usuario precisa se autenticar para entrar no sistema
    Given O usuario esta no site do sistema
    When Eu informo "<email>" e "<password>"
    Then O sistema notifica "<notify_message>"
    Examples:
      | email                 | password    | notify_message      |
      | teste@                | 123456      | Email Inválido      |
      | teste@teste.com.br    | 1q2w3e4r    | Usuário não existe. |