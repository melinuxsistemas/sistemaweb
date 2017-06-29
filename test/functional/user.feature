Feature: Usuario
    Scenario Outline: O usuario precisa se autenticar para entrar no sistema
    Given O usuario esta no site do sistema
    When Eu informo "<email>" e "<password>"
    Then O sistema notifica "<notify_message>"
    Examples:
      | email                 | password    | notify_message      |
      | teste@                | 123456      | Email Inválido      |
      | teste@teste.com.br    | 1q2w3e4r    | Usuário não existe. |


  Scenario Outline: O usuario precisa se registrar no sistema
    Given O usuario esta no site do sistema e acessa registrar
    When  Eu digito email "<email>" e "<password>" e "<confirm_password>"
    Then  O sistema retorna "<notify_message_register>"
    Examples:
      |email                      |password |confirm_password |notify_message_register    |
      |gianordolilucas@gmail.com  |1q2w3e4r |1q2w3e4r         |Falha na operação          |
      |teste@teste                |1q2w3e4r |1q2w3e4r         |Email Inválido             |
      |teste@teste.com            |11111111 |11111111         |Senhas Insegura            |
      |teste@teste.com            |1234abcd |1q2w3e4r         |Senhas não conferem        |


  Scenario Outline: O usuario pode trocar a senha de sua conta

    Given O usuario esta na pagina de login do sistema
    When O usuario digita senha atual "<old_password>" e "<password>" e "<confirm_password>"
    Then O sistema informa "<notify_message_change>".
    Examples:
      | old_password | password | confirm_password | notify_message_change |
      |1q2w3e4r      |abcd1234  |1234abcd          |Senhas não conferem                   |
      |abcd1234      |11111111  |11111111          |Informe numeros e letras            |
      |1q2w3e4r      |1q2w3e4r  |1q2w3e4r          |Nova Senha: Precisa ser diferente da senha antiga.|




