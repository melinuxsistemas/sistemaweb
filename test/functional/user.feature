Feature: Usuario

  Scenario Outline: O usuario precisa se autenticar para entrar no sistema
    Given O usuario esta no site do sistema
    When Eu informo "<email>" e "<password>"
    Then O sistema notifica "<notify_message>"
    Examples:
      | email                 | password    | notify_message      |
      | teste@                | 123456      | Email Inválido      |
      | teste@teste.com.br    | 1q2w3e4r    | Usuário não existe. |


  Scenario Outline: O usuario precisa ser registrado no sistema

    Given O usuario esta no site do sistema e acessa registrar
    When Eu digito email "<email>" e "<password>" e "<confirm_password>"
    Then O sistema informa "<notify_message_register>"


  Examples:
    | email                        | password      | confirm_password   | notify_message_register|
    |gianordolilucas@gmail.com     |1q2w3e4r       |1q2w3e4r            |ja cadastrado           |
    |emailinvalido@test.com        |1q2w3e4r       |1q2w3e4r            |email invalido          |
    |teste@teste.com               |11111111       |11111111            |senha invalida          |
    |teste@teste.com               |1q2w3e4r       |abcd1234            |senhas diferentes       |