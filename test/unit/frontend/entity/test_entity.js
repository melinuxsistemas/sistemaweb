/**
 * Created by lucas on 04/08/2017.
 */

/*
 * Created by diego on 03/05/2017.
 */
/*QUnit.module('usuario.register.validations.email', {
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

QUnit.module('usuario.register.validations.password', {
});

QUnit.test("validar_senhas", function( assert ) {
  var fixture = $("#qunit-fixture");
  fixture.append("<input id='password' type='text' class='form-control' placeholder='Senha..' required />");
  fixture.append("<input id='confirm_password' type='text' class='form-control' placeholder='Confirme a Senha..' required />");

  document.getElementById('password').value = '';
  document.getElementById('confirm_password').value = '';

  assert.ok((validate_password('password') && compare_passwords('password','confirm_password')) == false, "Teste: Não permitir campo senha vazio (OK) ");

  document.getElementById('password').value = '123';
  document.getElementById('confirm_password').value = '123';
  assert.ok((validate_password('password') && compare_passwords('password','confirm_password')) == false, "Teste: Não permitir senhas curtas (OK) ");

  document.getElementById('password').value = '1qa2ws3ed';
  document.getElementById('confirm_password').value = '1qa2ws3ed4';
  assert.ok((validate_password('password') && compare_passwords('password','confirm_password')) == false, "Teste: Não permitir senhas diferentes (OK) ");

  document.getElementById('password').value = '12345678';
  document.getElementById('confirm_password').value = '12345678';
  assert.ok((validate_password('password') && compare_passwords('password','confirm_password')) == false, "Teste: Não permitir senhas contendo somento números (OK) ");

  document.getElementById('password').value = 'asdqwezxc';
  document.getElementById('confirm_password').value = 'asdqwezxc';
  assert.ok((validate_password('password') && compare_passwords('password','confirm_password')) == false, "Teste: Não permitir senhas contendo somento letras (OK) ");

  document.getElementById('password').value = '1q2w3e4r';
  document.getElementById('confirm_password').value = '1q2w3e4r';
  assert.ok((validate_password('password') && compare_passwords('password','confirm_password')) == true, "Teste: Permitir senhas contendo letras e números com mais de 8 caracteres (OK) ");
});

QUnit.module('usuario.register', {
});

QUnit.test("validate_form_register", function(assert ) {
  var fixture = $("#qunit-fixture");
  fixture.append("<input id='email' type='text' class='form-control' placeholder='Email..' required />");
  fixture.append("<input id='password' type='text' class='form-control' placeholder='Senha..' required />");
  fixture.append("<input id='confirm_password' type='text' class='form-control' placeholder='Confirme a Senha..' required />");

  document.getElementById('email').value = '';
  document.getElementById('password').value = '';
  document.getElementById('confirm_password').value = '';
  assert.ok(validate_form_register() == false, "Teste: Não permitir cadastro com campos vazio (OK) ");

  document.getElementById('email').value = 'teste@teste.com';
  document.getElementById('password').value = '';
  document.getElementById('confirm_password').value = '';
  assert.ok(validate_form_register() == false, "Teste: Não permitir cadastro somente com campo email preenchido (OK) ");

  document.getElementById('email').value = '';
  document.getElementById('password').value = '1q2w3e4r5t';
  document.getElementById('confirm_password').value = '';
  assert.ok(validate_form_register() == false, "Teste: Não permitir cadastro somente com campo senha preenchido (OK) ");

  document.getElementById('email').value = '';
  document.getElementById('password').value = '';
  document.getElementById('confirm_password').value = '1q2w3e4r5t';
  assert.ok(validate_form_register() == false, "Teste: Não permitir cadastro somente com campo 'confirme a senha' preenchido (OK) ");

  document.getElementById('email').value = 'teste@teste.com';
  document.getElementById('password').value = '1q2w3e4r5t';
  document.getElementById('confirm_password').value = '';
  assert.ok(validate_form_register() == false, "Teste: Não permitir cadastro somente com campo email e senha preenchido (OK) ");

  document.getElementById('email').value = 'teste@teste.com';
  document.getElementById('password').value = '';
  document.getElementById('confirm_password').value = '1q2w3e4r5t';
  assert.ok(validate_form_register() == false, "Teste: Não permitir cadastro somente com campo email e 'confirme a senha' preenchido (OK) ");

  document.getElementById('email').value = '';
  document.getElementById('password').value = '1q2w3e4r5t';
  document.getElementById('confirm_password').value = '1q2w3e4r5t';
  assert.ok(validate_form_register() == false, "Teste: Não permitir cadastro somente com campo senha e 'confirme a senha' preenchido (OK) ");

  document.getElementById('email').value = 'teste@teste.com';
  document.getElementById('password').value = '1q2w3e4r5t';
  document.getElementById('confirm_password').value = '1q2w3e4r5t';
  assert.ok(validate_form_register() == true, "Teste: Permitir cadastro somente com todos os campos preenchido (OK) ");
});

QUnit.module('usuario.login', {
});
*/
QUnit.module('entity.register', {
});
QUnit.test("validate_form_regiter_person", function(assert ) {


  var fixture = $("#qunit-fixture");
  fixture.append('<form id="form-save-entity" autocomplete="off" ng-submit="save_person()" novalidate>');
  fixture.append('<div class="form-group field field_required" id="field_cpf_cnpj"><sub><label id="lb_cpf_cnpj" for="cpf_cnpj">CPF</label></sub><input name="cpf_cnpj" id="cpf_cnpj" class="form-control  ng-pristine ng-empty ng-invalid ng-invalid-required ng-valid-maxlength ng-touched" autocomplete="off" ng-model="cpf_cnpj" required="" maxlength="32" type="text"> <div class="alert"> </div> </div>');
  fixture.append('<div class="form-group field field_required" id="field_entity_name"><sub><label id="lb_entity_name" for="entity_name">Nome Completo</label></sub><input name="entity_name" id="entity_name" class="form-control  ng-pristine ng-empty ng-invalid ng-invalid-required ng-valid-maxlength ng-touched" autocomplete="off" ng-model="entity_name" required="" data-validate-length-range="6" maxlength="64" type="text"> <div class="alert"> </div> </div>');
  fixture.append('<div class="form-group field field_required" id="field_fantasy_name"><sub><label id="lb_fantasy_name" for="fantasy_name">Nome Fantasia</label></sub><input name="fantasy_name" id="fantasy_name" class="form-control  ng-pristine ng-valid ng-empty ng-valid-maxlength ng-touched" autocomplete="off" ng-model="fantasy_name" maxlength="32" type="text"> <div class="alert"> </div> </div>');
  fixture.append('<div class="form-group field field_required" id="field_birth_date_foundation"><sub><label id="lb_birth_date_foundation" for="birth_date_foundation">Data de Nascimento</label></sub><input name="birth_date_foundation" id="birth_date_foundation" class="form-control  ng-pristine ng-empty ng-invalid ng-invalid-required ng-touched" ng-model="birth_date_foundation" required="required" type="text"> <div class="alert"> </div> </div>');
  fixture.append('</form>');

  document.getElementById('cpf_cnpj').value = '';
  document.getElementById('entity_name').value = '';
  document.getElementById('fantasy_name').value = '';
  document.getElementById('birth_date_foundation').value = '';
  assert.ok(validate_form_regiter_person() == false, "Teste: Não permitir cadastro com campos vazio (OK) ");

  document.getElementById('cpf_cnpj').value = '11111111111';
  document.getElementById('entity_name').value = 'Teste teste';
  document.getElementById('fantasy_name').value = 'teste';
  document.getElementById('birth_date_foundation').value = '01/01/1998';
  assert.ok(validate_form_regiter_person() == false, "Teste: Não permite cpf inválidos (OK) ");

  document.getElementById('cpf_cnpj').value = '38141674226';
  document.getElementById('entity_name').value = 'Teste';
  document.getElementById('fantasy_name').value = 'Teste';
  document.getElementById('birth_date_foundation').value = '01/01/1998';
  assert.ok(validate_form_regiter_person() == false, "Teste: Não permitir cadastro com somente uma palavra (OK) ");

  document.getElementById('cpf_cnpj').value = '38141674226';
  document.getElementById('entity_name').value = '';
  document.getElementById('fantasy_name').value = '';
  document.getElementById('birth_date_foundation').value = '';
  assert.ok(validate_form_regiter_person() == false, "Teste: Não permitir cadastro com campos vazio (OK) ");

  document.getElementById('cpf_cnpj').value = '38141674226';
  document.getElementById('entity_name').value = '';
  document.getElementById('fantasy_name').value = '';
  document.getElementById('birth_date_foundation').value = '';
  assert.ok(validate_form_regiter_person() == false, "Teste: Não permitir cadastro com campos vazio (OK) ");

  document.getElementById('cpf_cnpj').value = '38141674226';
  document.getElementById('entity_name').value = '';
  document.getElementById('fantasy_name').value = '';
  document.getElementById('birth_date_foundation').value = '';
  assert.ok(validate_form_regiter_person() == false, "Teste: Não permitir cadastro com campos vazio (OK) ");

  document.getElementById('cpf_cnpj').value = '38141674226';
  document.getElementById('entity_name').value = 'Teste Teste';
  document.getElementById('fantasy_name').value = 'Teste';
  document.getElementById('birth_date_foundation').value = '01011998';
  assert.ok(validate_form_regiter_person() == true, "Teste: Não permitir cadastro com campos vazio (OK) ");
    /*
  document.getElementById('email').value = 'teste@teste.com';
  document.getElementById('password').value = '';
  assert.ok(validate_form_login() == false, "Teste: Não permitir cadastro somente com campo email preenchido (OK) ");

  document.getElementById('email').value = '';
  document.getElementById('password').value = '1q2w3e4r5t';
  assert.ok(validate_form_login() == false, "Teste: Não permitir cadastro somente com campo senha preenchido (OK) ");

  document.getElementById('email').value = 'teste@teste.com';
  document.getElementById('password').value = 'qwertyuias';
  assert.ok(validate_form_login() == false, "Teste: Não permitir senha somente com letras (OK) ");

  document.getElementById('email').value = 'teste@teste.com';
  document.getElementById('password').value = '1234567890';
  assert.ok(validate_form_login() == false, "Teste: Não permitir senha somente com numeros (OK) ");

  document.getElementById('email').value = 'teste@teste.com';
  document.getElementById('password').value = '1q3w4r6';
  assert.ok(validate_form_login() == false, "Teste: Não permitir senha com menos de 8 digitos (OK) ");

  document.getElementById('email').value = 'teste@teste';
  document.getElementById('password').value = '1q3er456yty';
  assert.ok(validate_form_login() == false, "Teste: Não permitir email sem .com ou .com.br (OK) ");

  document.getElementById('email').value = 'teste2teste';
  document.getElementById('password').value = '1q3er456yty';
  assert.ok(validate_form_login() == false, "Teste: Não permitir email sem o prefixo @ (OK) ");

  document.getElementById('email').value = 'teste@teste.com';
  document.getElementById('password').value = '1q2w3e4r5t';
  assert.ok(validate_form_login() == true, "Teste: Permitir cadastro somente com todos os campos preenchido (OK) ");
*/
});