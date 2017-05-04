/**
 * Created by diego on 03/05/2017.
 */

QUnit.module('core.base.notify', {
});

QUnit.test("show_information", function( assert ) {
  assert.ok(success_notify("Testando Notificações","Testando componente: success_notify") == true, "Teste: Apresentar notificação de Sucesso (OK) ");
  assert.ok(info_notify("Testando Notificações","Testando componente: info_notify") == true, "Teste: Apresentar notificação de Informação (OK) ");

  var fixture = $( "#qunit-fixture" );
  fixture.append( "<input id='teste'>hello!</input>" );
  assert.ok(warning_notify('teste',"Testando Notificações","Testando componente: warning_notify") == true, "Teste: Apresentar notificação de Aviso (OK) " );
  assert.ok(error_notify('teste',"Testando Notificações","Testando componente: error_notify") == false, "Teste: Apresentar notificação de Erro (OK) " );
});

QUnit.module('core.base.validations', {
});

QUnit.test("contains_numeric", function( assert ) {
  var teste_id = 'teste'
  var fixture = $( "#qunit-fixture" );
  fixture.append( "<input id='teste' value=''>hello!</input>");
  assert.ok(contains_numeric(teste_id) == false, "Teste: Verificar em um campo vazio (OK) " );

  document.getElementById(teste_id).value = 'ABCDEFGHIJ';
  assert.ok(contains_numeric(teste_id) == false, "Teste: Verificar em um campo somente com palavras (OK) " );

  document.getElementById(teste_id).value = 'ABCD13EFGH';
  assert.ok(contains_numeric(teste_id) == true, "Teste: Verificar em um campo contendo letras e números (OK) ");

  document.getElementById(teste_id).value = '1234567890';
  assert.ok(contains_numeric(teste_id) == true, "Teste: Verificar em um campo somente com números (OK) ");
});

QUnit.test("contains_alpha", function( assert ) {
  var teste_id = 'teste'
  var fixture = $( "#qunit-fixture" );
  fixture.append( "<input id='teste' value=''>hello!</input>");
  assert.ok(contains_alpha(teste_id) == false, "Teste: Verificar em um campo vazio (OK) ");

  document.getElementById(teste_id).value = '1234567890';
  assert.ok(contains_alpha(teste_id) == false, "Teste: Verificar em um campo somente com numeros (OK) ");

  document.getElementById(teste_id).value = '12ABCDEFGH';
  assert.ok(contains_alpha(teste_id) == true, "Teste: Verificar em um campo contendo letras e números (OK) " );

  document.getElementById(teste_id).value = 'ABCDEFGHIJK';
  assert.ok(contains_alpha(teste_id) == true, "Teste: Verificar em um campo somente com palavras (OK) " );
});

QUnit.test("is_empty", function( assert ) {
  var teste_id = 'teste'
  var fixture = $("#qunit-fixture");
  fixture.append("<input id='teste' value=''>hello!</input>");
  assert.ok(is_empty(teste_id) == true, "Teste: Verificar em um campo vazio (OK) ");

  document.getElementById(teste_id).value = '1234567890';
  assert.ok(is_empty(teste_id) == false, "Teste: Verificar em um campo preenchido (OK) ");
});

QUnit.test("contains_minimal_size", function( assert ) {
  var teste_id = 'teste'
  var fixture = $("#qunit-fixture");
  fixture.append("<input id='teste' value=''>hello!</input>");
  assert.ok(contains_minimal_size(teste_id,8) == false, "Teste: Verificar em um campo vazio (OK) ");

  document.getElementById(teste_id).value = '123456';
  assert.ok(contains_minimal_size(teste_id,8) == false, "Teste: Verificar em um campo com menos caracteres que o mínimo (OK) ");

  document.getElementById(teste_id).value = '12345678';
  assert.ok(contains_minimal_size(teste_id,8) == true, "Teste: Verificar em um campo com exatamente a mesma quantidade caracteres que o mínimo (OK) ");

  document.getElementById(teste_id).value = '1234567810';
  assert.ok(contains_minimal_size(teste_id,8) == true, "Teste: Verificar em um campo com mais caracteres que o mínimo (OK) ");
});