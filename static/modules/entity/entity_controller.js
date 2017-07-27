/**
 * Created by diego on 05/05/2017.
 */
var application = angular.module('modules.entity', []);

/*
application.controller('register_controller', function($scope) {

  success_function = function(){
      success_notify("Operação realizada com Sucesso!","Verifique seu email, você receberá um email em instantes.")
  }

  $scope.reset_password = function () {
    var data_paramters = {email: $scope.email}
    request_api("/api/user/reset_password",data_paramters,validate_form_reset_password,success_function,null)
  }

  $scope.resend_activation_code = function () {
    var data_paramters = {email: $scope.email}
    request_api("/api/user/reactivate",data_paramters,validate_form_reset_password,success_function,null)
  }
});

application.controller('change_password_controller', function($scope) {

  $scope.save_password = function () {
    var data_paramters = {
      old_password: $scope.old_password,
      password:  $scope.password,
      confirm_password:  $scope.confirm_password
    }

    success_function = function(){
      success_notify("Operação realizada com Sucesso!","Senha de acesso redefinida.")
      $("#old_password").val("")
      $("#password").val("")
      $("#confirm_password").val("")
      $scope.old_password = "";
      $scope.password = "";
      $scope.confirm_password = "";
    }

    request_api("/api/user/change_password",data_paramters,validate_form_change_password,success_function,null)
  }
});
*/
application.controller('register_person_controller', function($scope) {
  $scope.cpf_cnpj = "";
  $scope.entity_name = "";
  $scope.fantasy_name = "";
  $scope.confirm_password = "";
  $scope.birth_date_foundation = "";


  $scope.save_person = function () {
      $scope.cpf_cnpj = $('#cpf_cnpj').val()
      $scope.birth_date_foundation = $('#birth_date_foundation').val()
    var data_paramters = {
      entity_type: 'PF',
      cpf_cnpj: $scope.cpf_cnpj,
      entity_name: $scope.entity_name,
      fantasy_name: $scope.fantasy_name,
      birth_date_foundation: $scope.birth_date_foundation,
    }
    success_function = function(){
      //window.location = "/"//register/confirm/"+$scope.email;
      alert("Beleza")
    }
    request_api("/api/entity/register/person/save",data_paramters,validate_date($scope.birth_date_foundation),function () {
      return true;
    },success_function,null)
  }
});
/*
  $scope.resend_activation_code = function () {
    var data_paramters = {email: $scope.email}
    $("#email").val($scope.email)
    success_function = function(){
      confirm_notify("Operação realizada com Sucesso!","Verifique seu email, você receberá um email em instantes.<br><a href='/login'>Clique aqui para acessar sistema.</a>")
    }
    request_api("/api/user/reactivate",data_paramters,validate_form_confirm_register,success_function,null)
  }
});


application.controller('login_controller', function($scope) {

  $scope.login_autentication = function () {
    var data_paramters = {email: $scope.email, password: $scope.password}
    success_function = function(){
      window.location = "/";
    }
    request_api("/api/user/login/autentication",data_paramters,validate_form_login,success_function,null)
  }
});
*/

/*
application.controller('entity_controller', function ($scope) {
  $scope.tipo_entidade = "";
  $scope.cpf_cnpj = "";
  $scope.nome_razao = "";
  $scope.nome_fantasia = "";
  $scope.nasc_fundacao = "";

  $scope.save_entity = function () {
    var data_paramters = {
        tipo_entidade: $scope.tipo_entidade,
        cpf_cnpj: $scope.cpf_cnpj,
        nome_razao: $scope.nome_razao,
        nome_fantasia: $scope.nome_fantasia,
        nasc_fundacao: $scope.nasc_fundacao
    };
    success_function = function () {
      window.location = "/entidade/register/confirm"+$scope.cpf_cnpj;
    }
  }
});
*/