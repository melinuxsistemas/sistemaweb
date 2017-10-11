/**
 * Created by lucas on 04/08/2017.
 */

QUnit.module('entity.register', {
});
QUnit.test("validate_form_regiter_person", function(assert ) {
  var fixture = $("#qunit-fixture");                              //ng-pristine ng-empty ng-invalid  ng-valid-maxlength ng-touched
  fixture.append('<div class="form-group field field_required" id="field_cpf_cnpj"><sub><label id="lb_cpf_cnpj" for="cpf_cnpj">CPF</label></sub><input name="cpf_cnpj" id="cpf_cnpj" class="form-control ng-invalid-required " autocomplete="off" ng-model="cpf_cnpj " required="required" maxlength="32" type="text"> <div class="alert"> </div> </div>');
  fixture.append('<div class="form-group field field_required" id="field_entity_name"><sub><label id="lb_entity_name" for="entity_name">Nome Completo</label></sub><input name="entity_name" id="entity_name" class="form-control  ng-pristine ng-empty ng-invalid ng-invalid-required ng-valid-maxlength ng-touched" autocomplete="off" ng-model="entity_name" required="true" data-validate-length-range="6" maxlength="64" type="text" required> <div class="alert"> </div> </div>');
  fixture.append('<div class="form-group field field_required" id="field_fantasy_name"><sub><label id="lb_fantasy_name" for="fantasy_name">Nome Fantasia</label></sub><input name="fantasy_name" id="fantasy_name" class="form-control  ng-pristine ng-valid ng-empty ng-valid-maxlength ng-touched" autocomplete="off" ng-model="fantasy_name" maxlength="32" type="text"> <div class="alert"> </div> </div>');
  fixture.append('<div class="form-group field field_required" id="field_birth_date_foundation"><sub><label id="lb_birth_date_foundation" for="birth_date_foundation">Data de Nascimento</label></sub><input name="birth_date_foundation" id="birth_date_foundation" class="form-control  ng-pristine ng-empty ng-invalid ng-invalid-required ng-touched" ng-model="birth_date_foundation" required="required" type="text"> <div class="alert"> </div> </div>');


  document.getElementById('cpf_cnpj').value = '11111111111';
  document.getElementById('entity_name').value = 'Teste teste';
  document.getElementById('fantasy_name').value = 'teste';
  document.getElementById('birth_date_foundation').value = '01/01/1990';
  assert.ok(validate_form_regiter_person() == false, "Teste: Não permite cpf inválidos (OK) ");

  document.getElementById('cpf_cnpj').value = '';
  document.getElementById('entity_name').value = '';
  document.getElementById('fantasy_name').value = '';
  document.getElementById('birth_date_foundation').value = '01/08/1995';
  assert.ok(validate_form_regiter_person() == false, "Teste: Não permitir com campo Nome vazio (OK) ");

  document.getElementById('cpf_cnpj').value = '38141674226';
  document.getElementById('entity_name').value = 'teste teste';
  document.getElementById('fantasy_name').value = '';
  document.getElementById('birth_date_foundation').value = '01/50/2500';
  assert.ok(validate_form_regiter_person() == false, "Teste: Não permitir cadastro de datas futuras (OK) ");

  document.getElementById('cpf_cnpj').value = '38141674226';
  document.getElementById('entity_name').value = 'teste teste';
  document.getElementById('fantasy_name').value = '';
  document.getElementById('birth_date_foundation').value = '01/50/1000';
  assert.ok(validate_form_regiter_person() == false, "Teste: Não permitir cadastro de pessoas com mais de 150 anos (OK) ");

  document.getElementById('cpf_cnpj').value = '38141674226';
  document.getElementById('entity_name').value = 'Teste Teste';
  document.getElementById('fantasy_name').value = 'Teste';
  document.getElementById('birth_date_foundation').value = '01/01/1998';
  assert.ok(validate_form_regiter_person() == true, "Teste: Possui todos dados conforme o padrão desejado (OK) ");

  document.getElementById('cpf_cnpj').value = '38141674226';
  document.getElementById('entity_name').value = 'Teste Teste';
  document.getElementById('fantasy_name').value = '';
  document.getElementById('birth_date_foundation').value = '';
  assert.ok(validate_form_regiter_person() == true, "Teste: Permitir cadastro somente com campos obrigatórios preenchidos (OK) ");

});

QUnit.module('entity.contact.register', {
})

QUnit.test("validate_contact", function(assert ) {
  var fixture = $("#qunit-fixture");
  fixture.append('<div class="form-group field field_required" id="field_type_contact"><sub><label id="lb_type_contact" for="type_contact">Tipo de contato</label></sub><br><input name="type_contact" id="type_contact" class="form-control" maxlength="10" required="" type="text"><div class="alert"></div></div>')
  fixture.append('<div class="form-group field field_required" id="field_name"><sub><label id="lb_name" for="name">Nome Completo</label></sub><br><input name="name" id="name_contact" class="form-control" required="" maxlength="30" type="text"> <div class="alert"></div></div>')
  fixture.append('<div class="form-group field field_required" id="field_ddd"><sub><label id="lb_ddd" for="ddd">DDD</label></sub><br><input name="ddd" id="ddd" class="form-control" required="" maxlength="4" type="text"><div class="alert"></div> </div>')
  fixture.append('<div class="form-group field field_required" id="field_phone"><sub><label id="lb_phone" for="phone">Telefone</label></sub><br><input name="phone" id="phone_number" class="form-control" required="" maxlength="10" type="text"><div class="alert"></div></div>')
  fixture.append('<div class="form-group field" id="field_complemento"><sub><label id="lb_complemento" for="complemento">Complemento</label> </sub><br><input name="complemento" id="complemento" class="form-control" maxlength="32" type="text"><div class="alert"></div></div>');


  document.getElementById('type_contact').value = 'FIXO';
  document.getElementById('name_contact').value = 'TESTE';
  document.getElementById('ddd').value = '27';
  document.getElementById('phone_number').value = '32325454';
  document.getElementById('complemento').value = 'COMPLET';
  assert.ok(validate_contact()==true,"Teste: Atende todos requesitos necessários para adicionar contato. (OK)")

  document.getElementById('type_contact').value = '';
  document.getElementById('name_contact').value = 'TESTE';
  document.getElementById('ddd').value = '27';
  document.getElementById('phone_number').value = '32325454';
  document.getElementById('complemento').value = '';
  assert.ok(validate_contact()==true,"Teste: Campos que podem ser vazios. (OK)")

  document.getElementById('type_contact').value = 'FIXO';
  document.getElementById('name_contact').value = '';
  document.getElementById('ddd').value = '27';
  document.getElementById('phone_number').value = '32325454';
  document.getElementById('complemento').value = 'COMPLET';
  assert.ok(validate_contact()==false,"Teste: Não se pode ter contato sem nome. (OK)")

  document.getElementById('type_contact').value = 'FIXO';
  document.getElementById('name_contact').value = 'TESTE';
  document.getElementById('ddd').value = '';
  document.getElementById('phone_number').value = '32325454';
  document.getElementById('complemento').value = 'COMPLET';
  assert.ok(validate_contact()==false,"Teste: Não se pode ter contato sem ddd. (OK)")

  document.getElementById('type_contact').value = 'FIXO';
  document.getElementById('name_contact').value = 'TESTE';
  document.getElementById('ddd').value = '27';
  document.getElementById('phone_number').value = '';
  document.getElementById('complemento').value = 'COMPLET';
  assert.ok(validate_contact()==false,"Teste: Não se pode ter contato sem telefone. (OK)")


  document.getElementById('type_contact').value = 'FIXO';
  document.getElementById('name_contact').value = 'TESTE';
  document.getElementById('ddd').value = null;
  document.getElementById('phone_number').value = '32325454';
  document.getElementById('complemento').value = 'COMPLET';
  assert.ok(validate_contact()==false,"Teste: Não se pode ter contato sem ddd. (OK)")


  document.getElementById('type_contact').value = 'FIXO';
  document.getElementById('name_contact').value = null;
  document.getElementById('ddd').value = '27';
  document.getElementById('phone_number').value = '32325454';
  document.getElementById('complemento').value = 'COMPLET';
  assert.ok(validate_contact()==false,"Teste: Não se pode ter contato sem nome. (OK)")


  document.getElementById('type_contact').value = 'FIXO';
  document.getElementById('name_contact').value = 'TESTE';
  document.getElementById('ddd').value = '27';
  document.getElementById('phone_number').value = null;
  document.getElementById('complemento').value = 'COMPLET';
  assert.ok(validate_contact()==false,"Teste: Não se pode ter contato sem telefone. (OK)")

});

QUnit.module('entity.Email.register', {
});

QUnit.test("validate_email", function(assert ) {

  var fixture = $("#qunit-fixture");
  fixture.append('<input name="email" class="form-control text-lowercase ng-pristine ng-empty ng-invalid ng-invalid-required ng-valid-maxlength ng-touched" id="email" ng-model="email" autocomplete="off" placeholder="Email.." required="" maxlength="256" type="text">');
  fixture.append('<input name="name" id="name" class="form-control ng-valid-maxlength ng-dirty ng-valid-parse ng-empty ng-invalid ng-invalid-required ng-touched" ng-model="name" placeholder="Nome.." autocomplete="off" maxlength="30" required="" type="text">');
  fixture.append('<select name="send_xml" id="send_xml" class="form_control"><option value="True">Sim</option><option value="False">Não</option></select>');
  fixture.append('<select name="send_suitcase" id="send_suitcase" class="send_suitcase"><option value="True">Sim</option><option value="False">Não</option></select>');


  document.getElementById('email').value = 'teste@teste.com';
  document.getElementById('name').value = 'TESTE';
  document.getElementById('send_xml').value = 'True';
  document.getElementById('send_suitcase').value = 'True';
  assert.ok(validate_email()==true,"Teste: Atende todos requisitos para adicionar um email. (OK)")

  document.getElementById('email').value = '';
  document.getElementById('name').value = 'TESTE';
  document.getElementById('send_xml').value = 'True';
  document.getElementById('send_suitcase').value = 'True';
  assert.ok(validate_email()==false,"Teste: Campo email não pode ser vazio. (OK)");

  document.getElementById('email').value = null;
  document.getElementById('name').value = 'TESTE';
  document.getElementById('send_xml').value = 'True';
  document.getElementById('send_suitcase').value = 'True';
  assert.ok(validate_email()==false,"Teste: Campo email não pode ser nulo. (OK)")

  document.getElementById('email').value = 'teste@teste.com';
  document.getElementById('name').value = '';
  document.getElementById('send_xml').value = 'True';
  document.getElementById('send_suitcase').value = 'True';
  assert.ok(validate_email()==false,"Teste: Campo nome não pode ser vazio. (OK)")

  document.getElementById('email').value = 'teste@teste.com';
  document.getElementById('name').value = null;
  document.getElementById('send_xml').value = 'True';
  document.getElementById('send_suitcase').value = 'True';
  assert.ok(validate_email()==false,"Teste: Campo nome não pode ser nulo. (OK)")

  document.getElementById('email').value = 'teste@teste.com';
  document.getElementById('name').value = 'Teste teste';
  document.getElementById('send_xml').value = '';
  document.getElementById('send_suitcase').value = 'True';
  assert.ok(validate_email()==false,"Teste: Campo send_xml não pode ser vazio. (OK)")

  document.getElementById('email').value = 'teste@teste.com';
  document.getElementById('name').value = 'Teste teste';
  document.getElementById('send_xml').value = null;
  document.getElementById('send_suitcase').value = 'True';
  assert.ok(validate_email()==false,"Teste: Campo send_xml não pode ser nulo. (OK)")

  document.getElementById('email').value = 'teste@teste.com';
  document.getElementById('name').value = 'Teste teste';
  document.getElementById('send_xml').value = 'True';
  document.getElementById('send_suitcase').value = '';
  assert.ok(validate_email()==false,"Teste: Campo send_suitcase não pode ser vazio. (OK)")

  document.getElementById('email').value = 'teste@teste.com';
  document.getElementById('name').value = 'Teste teste';
  document.getElementById('send_xml').value = 'True';
  document.getElementById('send_suitcase').value = null;
  assert.ok(validate_email()==false,"Teste: Campo send_suitcase não pode ser nulo. (OK)")

});