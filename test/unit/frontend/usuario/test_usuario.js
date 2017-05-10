/**
 * Created by diego on 03/05/2017.
 */
QUnit.module('usuario.register.validations.email', {
});
//validate_form_register

QUnit.test("email_is_valid", function( assert ) {
  var fixture = $("#qunit-fixture");
  fixture.append("<input id='email' type='text' class='form-control' placeholder='Email..' required />");
  document.getElementById('email').value = '';
  assert.ok(email_is_valid('email') == false, "Teste: Não permitir campo vazio (OK) ");

  document.getElementById('email').value = 'teste@';
  assert.ok(email_is_valid('email') == false, "Teste: Não permitir email inválido (OK) ");

  document.getElementById('email').value = 'teste@teste.com';
  assert.ok(email_is_valid('email') == true, "Teste: Permitir email válido (OK) ");
});

QUnit.module('usuario.register.validations.email', {
});

QUnit.test("validar_senhas", function( assert ) {
  var fixture = $("#qunit-fixture");
  fixture.append("<input id='senha' type='text' class='form-control' placeholder='Senha..' required />");
  fixture.append("<input id='confirma_senha' type='text' class='form-control' placeholder='Confirme a Senha..' required />");

  document.getElementById('senha').value = '';
  document.getElementById('confirma_senha').value = '';

  assert.ok((validate_password('senha') && compare_passwords('senha','confirma_senha')) == false, "Teste: Não permitir campo senha vazio (OK) ");

  document.getElementById('senha').value = '123';
  document.getElementById('confirma_senha').value = '123';
  assert.ok((validate_password('senha') && compare_passwords('senha','confirma_senha')) == false, "Teste: Não permitir senhas curtas (OK) ");

  document.getElementById('senha').value = '1qa2ws3ed';
  document.getElementById('confirma_senha').value = '1qa2ws3ed4';
  assert.ok((validate_password('senha') && compare_passwords('senha','confirma_senha')) == false, "Teste: Não permitir senhas diferentes (OK) ");

  document.getElementById('senha').value = '12345678';
  document.getElementById('confirma_senha').value = '12345678';
  assert.ok((validate_password('senha') && compare_passwords('senha','confirma_senha')) == false, "Teste: Não permitir senhas contendo somento números (OK) ");

  document.getElementById('senha').value = 'asdqwezxc';
  document.getElementById('confirma_senha').value = 'asdqwezxc';
  assert.ok((validate_password('senha') && compare_passwords('senha','confirma_senha')) == false, "Teste: Não permitir senhas contendo somento letras (OK) ");

  document.getElementById('senha').value = '1q2w3e4r';
  document.getElementById('confirma_senha').value = '1q2w3e4r';
  assert.ok((validate_password('senha') && compare_passwords('senha','confirma_senha')) == true, "Teste: Permitir senhas contendo letras e números com mais de 8 caracteres (OK) ");
});

QUnit.module('usuario.register', {
});

QUnit.test("validate_form_register", function(assert ) {
  var fixture = $("#qunit-fixture");
  fixture.append("<input id='email' type='text' class='form-control' placeholder='Email..' required />");
  fixture.append("<input id='senha' type='text' class='form-control' placeholder='Senha..' required />");
  fixture.append("<input id='confirma_senha' type='text' class='form-control' placeholder='Confirme a Senha..' required />");

  document.getElementById('email').value = '';
  document.getElementById('senha').value = '';
  document.getElementById('confirma_senha').value = '';
  assert.ok(validate_form_register() == false, "Teste: Não permitir cadastro com campos vazio (OK) ");

  document.getElementById('email').value = 'teste@teste.com';
  document.getElementById('senha').value = '';
  document.getElementById('confirma_senha').value = '';
  assert.ok(validate_form_register() == false, "Teste: Não permitir cadastro somente com campo email preenchido (OK) ");

  document.getElementById('email').value = '';
  document.getElementById('senha').value = '1q2w3e4r5t';
  document.getElementById('confirma_senha').value = '';
  assert.ok(validate_form_register() == false, "Teste: Não permitir cadastro somente com campo senha preenchido (OK) ");

  document.getElementById('email').value = '';
  document.getElementById('senha').value = '';
  document.getElementById('confirma_senha').value = '1q2w3e4r5t';
  assert.ok(validate_form_register() == false, "Teste: Não permitir cadastro somente com campo 'confirme a senha' preenchido (OK) ");

  document.getElementById('email').value = 'teste@teste.com';
  document.getElementById('senha').value = '1q2w3e4r5t';
  document.getElementById('confirma_senha').value = '';
  assert.ok(validate_form_register() == false, "Teste: Não permitir cadastro somente com campo email e senha preenchido (OK) ");

  document.getElementById('email').value = 'teste@teste.com';
  document.getElementById('senha').value = '';
  document.getElementById('confirma_senha').value = '1q2w3e4r5t';
  assert.ok(validate_form_register() == false, "Teste: Não permitir cadastro somente com campo email e 'confirme a senha' preenchido (OK) ");

  document.getElementById('email').value = '';
  document.getElementById('senha').value = '1q2w3e4r5t';
  document.getElementById('confirma_senha').value = '1q2w3e4r5t';
  assert.ok(validate_form_register() == false, "Teste: Não permitir cadastro somente com campo senha e 'confirme a senha' preenchido (OK) ");

  document.getElementById('email').value = 'teste@teste.com';
  document.getElementById('senha').value = '1q2w3e4r5t';
  document.getElementById('confirma_senha').value = '1q2w3e4r5t';
  assert.ok(validate_form_register() == true, "Teste: Permitir cadastro somente com todos os campos preenchido (OK) ");
});