/**
 * Created by diego on 03/05/2017.
 */
QUnit.module('usuario.register.validations.email', {
  
});
//validar_formulario

QUnit.test("validar_email", function( assert ) {
  var fixture = $("#qunit-fixture");
  fixture.append("<input id='email' type='text' class='form-control' placeholder='Email..' required />");
  document.getElementById('email').value = '';
  assert.ok(validar_email() == false, "Teste: Não permitir campo vazio (OK) ");

  document.getElementById('email').value = 'teste@';
  assert.ok(validar_email() == false, "Teste: Não permitir email inválido (OK) ");

  document.getElementById('email').value = 'teste@teste.com';
  assert.ok(validar_email() == true, "Teste: Permitir email válido (OK) ");
});

QUnit.module('usuario.register.validations.email', {

});

QUnit.test("validar_senhas", function( assert ) {
  var fixture = $("#qunit-fixture");
  fixture.append("<input id='senha' type='text' class='form-control' placeholder='Senha..' required />");
  fixture.append("<input id='re_senha' type='text' class='form-control' placeholder='Confirme a Senha..' required />");

  document.getElementById('senha').value = '';
  document.getElementById('re_senha').value = '';
  assert.ok(validar_senha() == false, "Teste: Não permitir campo senha vazio (OK) ");

  document.getElementById('senha').value = '123';
  document.getElementById('re_senha').value = '123';
  assert.ok(validar_senha() == false, "Teste: Não permitir senhas curtas (OK) ");

  document.getElementById('senha').value = '1qa2ws3ed';
  document.getElementById('re_senha').value = '1qa2ws3ed4';
  assert.ok(validar_senha() == false, "Teste: Não permitir senhas diferentes (OK) ");

  document.getElementById('senha').value = '12345678';
  document.getElementById('re_senha').value = '12345678';
  assert.ok(validar_senha() == false, "Teste: Não permitir senhas contendo somento números (OK) ");

  document.getElementById('senha').value = 'asdqwezxc';
  document.getElementById('re_senha').value = 'asdqwezxc';
  assert.ok(validar_senha() == false, "Teste: Não permitir senhas contendo somento letras (OK) ");

  document.getElementById('senha').value = '1q2w3e4r';
  document.getElementById('re_senha').value = '1q2w3e4r';
  assert.ok(validar_senha() == true, "Teste: Permitir senhas contendo letras e números com mais de 8 caracteres (OK) ");
});

QUnit.module('usuario.register', {

});

QUnit.test("validar_formulario", function( assert ) {
  var fixture = $("#qunit-fixture");
  fixture.append("<input id='email' type='text' class='form-control' placeholder='Email..' required />");
  fixture.append("<input id='senha' type='text' class='form-control' placeholder='Senha..' required />");
  fixture.append("<input id='re_senha' type='text' class='form-control' placeholder='Confirme a Senha..' required />");

  document.getElementById('email').value = '';
  document.getElementById('senha').value = '';
  document.getElementById('re_senha').value = '';
  assert.ok(validar_formulario() == false, "Teste: Não permitir cadastro com campos vazio (OK) ");

  document.getElementById('email').value = 'teste@teste.com';
  document.getElementById('senha').value = '';
  document.getElementById('re_senha').value = '';
  assert.ok(validar_formulario() == false, "Teste: Não permitir cadastro somente com campo email preenchido (OK) ");

  document.getElementById('email').value = '';
  document.getElementById('senha').value = '1q2w3e4r5t';
  document.getElementById('re_senha').value = '';
  assert.ok(validar_formulario() == false, "Teste: Não permitir cadastro somente com campo senha preenchido (OK) ");

  document.getElementById('email').value = '';
  document.getElementById('senha').value = '';
  document.getElementById('re_senha').value = '1q2w3e4r5t';
  assert.ok(validar_formulario() == false, "Teste: Não permitir cadastro somente com campo 'confirme a senha' preenchido (OK) ");

  document.getElementById('email').value = 'teste@teste.com';
  document.getElementById('senha').value = '1q2w3e4r5t';
  document.getElementById('re_senha').value = '';
  assert.ok(validar_formulario() == false, "Teste: Não permitir cadastro somente com campo email e senha preenchido (OK) ");

  document.getElementById('email').value = 'teste@teste.com';
  document.getElementById('senha').value = '';
  document.getElementById('re_senha').value = '1q2w3e4r5t';
  assert.ok(validar_formulario() == false, "Teste: Não permitir cadastro somente com campo email e 'confirme a senha' preenchido (OK) ");

  document.getElementById('email').value = '';
  document.getElementById('senha').value = '1q2w3e4r5t';
  document.getElementById('re_senha').value = '1q2w3e4r5t';
  assert.ok(validar_formulario() == false, "Teste: Não permitir cadastro somente com campo senha e 'confirme a senha' preenchido (OK) ");

  document.getElementById('email').value = 'teste@teste.com';
  document.getElementById('senha').value = '1q2w3e4r5t';
  document.getElementById('re_senha').value = '1q2w3e4r5t';
  assert.ok(validar_formulario() == true, "Teste: Permitir cadastro somente com todos os campos preenchido (OK) ");
});