/**
 * Created by lucas on 04/08/2017.
 */

QUnit.module('entity.register', {
});
QUnit.test("validate_form_regiter_person", function(assert ) {


  var fixture = $("#qunit-fixture");
  fixture.append('<form id="form-save-entity" autocomplete="off" ng-submit="save_person()" novalidate>');                                   //ng-pristine ng-empty ng-invalid  ng-valid-maxlength ng-touched
  fixture.append('<div class="form-group field field_required" id="field_cpf_cnpj"><sub><label id="lb_cpf_cnpj" for="cpf_cnpj">CPF</label></sub><input name="cpf_cnpj" id="cpf_cnpj" class="form-control ng-invalid-required " autocomplete="off" ng-model="cpf_cnpj " required="required" maxlength="32" type="text"> <div class="alert"> </div> </div>');
  fixture.append('<div class="form-group field field_required" id="field_entity_name"><sub><label id="lb_entity_name" for="entity_name">Nome Completo</label></sub><input name="entity_name" id="entity_name" class="form-control  ng-pristine ng-empty ng-invalid ng-invalid-required ng-valid-maxlength ng-touched" autocomplete="off" ng-model="entity_name" required="true" data-validate-length-range="6" maxlength="64" type="text" required> <div class="alert"> </div> </div>');
  fixture.append('<div class="form-group field field_required" id="field_fantasy_name"><sub><label id="lb_fantasy_name" for="fantasy_name">Nome Fantasia</label></sub><input name="fantasy_name" id="fantasy_name" class="form-control  ng-pristine ng-valid ng-empty ng-valid-maxlength ng-touched" autocomplete="off" ng-model="fantasy_name" maxlength="32" type="text"> <div class="alert"> </div> </div>');
  fixture.append('<div class="form-group field field_required" id="field_birth_date_foundation"><sub><label id="lb_birth_date_foundation" for="birth_date_foundation">Data de Nascimento</label></sub><input name="birth_date_foundation" id="birth_date_foundation" class="form-control  ng-pristine ng-empty ng-invalid ng-invalid-required ng-touched" ng-model="birth_date_foundation" required="required" type="text"> <div class="alert"> </div> </div>');

  fixture.append('</form>');
  /*Não esta conseguindo validar o form na func CheckAll dessa forma todas as especificações
    no Form.py d entidade não esta sendo validada, e espaços vazio são aceitos, palavra que excedão o tam. maximo
    O teste de campo sando a func:Validate_field_entity n funciona pois o fixture cria um campo do tipo hidden*/
  //alert("Olha o form criado"+JSON.stringify(fixture))
  //document.getElementById('cpf_cnpj').value = '';
  //document.getElementById('entity_name').value = '';
    /*var cpf_cnpj = $('#cpf_cnpj').val('')

    alert("Veja o controle: "+cpf_cnpj.val())
  assert.ok(validate_field_entity('cpf_cnpj') == false, "Teste: Não permitir cadastro com campos vazio (OK) ");*/

  /*document.getElementById('cpf_cnpj').value = '38141674226';
  document.getElementById('entity_name').value = 'teste';
  document.getElementById('fantasy_name').value = '';
  document.getElementById('birth_date_foundation').value = '';
  alert(JSON.stringify(document))
  assert.ok(validate_form_regiter_person() == false, "Teste: Não permitir cadastro com campos vazio (OK) ");*/


  document.getElementById('cpf_cnpj').value = '11111111111';
  document.getElementById('entity_name').value = 'Teste teste';
  document.getElementById('fantasy_name').value = 'teste';
  document.getElementById('birth_date_foundation').value = '01/01/1998';
  assert.ok(validate_form_regiter_person() == false, "Teste: Não permite cpf inválidos (OK) ");

  document.getElementById('cpf_cnpj').value = '38141674226';
  document.getElementById('entity_name').value = '';
  document.getElementById('fantasy_name').value = '';
  document.getElementById('birth_date_foundation').value = '01/50/2000';
  assert.ok(validate_form_regiter_person() == false, "Teste: Não permitir cadastro de pessoas menor de idade (OK) ");

  document.getElementById('cpf_cnpj').value = '38141674226';
  document.getElementById('entity_name').value = '';
  document.getElementById('fantasy_name').value = '';
  document.getElementById('birth_date_foundation').value = '01/50/2500';
  assert.ok(validate_form_regiter_person() == false, "Teste: Não permitir cadastro de datas futuras (OK) ");

  document.getElementById('cpf_cnpj').value = '38141674226';
  document.getElementById('entity_name').value = '';
  document.getElementById('fantasy_name').value = '';
  document.getElementById('birth_date_foundation').value = '01/50/1000';
  assert.ok(validate_form_regiter_person() == false, "Teste: Não permitir cadastro de pessoas com mais de 150 anos (OK) ");

  document.getElementById('cpf_cnpj').value = '38141674226';
  document.getElementById('entity_name').value = 'Teste Teste';
  document.getElementById('fantasy_name').value = 'Teste';
  document.getElementById('birth_date_foundation').value = '01/01/1998';
  assert.ok(validate_form_regiter_person() == true, "Teste: Possui todos dados conforme o padrão desejado (OK) ");

});