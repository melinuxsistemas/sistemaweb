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
    $scope.cpf_cnpj = $('#cpf_cnpj').val();
    $scope.birth_date_foundation = $('#birth_date_foundation').val();

    var data_paramters = {
      entity_type: 'PF',
      registration_status: 0,
      cpf_cnpj: clear_mask_numbers($scope.cpf_cnpj),
      entity_name: $scope.entity_name.toUpperCase(),
      fantasy_name: $scope.fantasy_name.toUpperCase(),
      birth_date_foundation: $scope.birth_date_foundation,
      comments: $scope.comments,
    }

    success_function = function(message){
      //window.location = "/"//register/confirm/"+$scope.email;
      check_response_message_form('#form-save-entity', message);
		}
    
    fail_function = function (message) {
      check_response_message_form('#form-save-entity', message);
      //notify('error','Formulário com dados inválidos',message.cpf_cnpj)
    }

    validade_function = function () {
     return  true;//validate_form_regiter_person(); //validate_date($scope.birth_date_foundation);
    }
    request_api("/api/entity/register/person/save",data_paramters,validade_function,success_function,fail_function)
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
*/

application.controller('register_company_controller', function ($scope) {
    $scope.cpf_cnpj = "";
    $scope.entity_name = "";
    $scope.fantasy_name = "";
    $scope.birth_date_foundation = "";

    $scope.save_company = function () {
        $scope.cpf_cnpj = $('#cpf_cnpj').val();
        $scope.birth_date_foundation = $('#birth_date_foundation').val();
        var data_paramters = {
            entity_type: 'PJ',
            cpf_cnpj: clear_mask_numbers($scope.cpf_cnpj),
            entity_name: $scope.entity_name,
            fantasy_name: $scope.fantasy_name,
            birth_date_foundation: $scope.birth_date_foundation,
        }
        success_function = function (message) {
            check_response_message_form('#form-save-company', message);
        }

        fail_function = function (message) {
            check_response_message_form('#form-save-company', message);
            notify('error', 'Formulário com dados inválidos', message)
        }
        request_api("/api/entity/register/company/save", data_paramters, validate_form_regiter_company, success_function, fail_function)

    };
});

application.controller('register_phone_entity', function ($scope) {
  $scope.save_tel = function (){
		alert('VINDO AQUI JÀ')
	}
});

application.controller('register_email_entity', function ($scope) {
  $scope.save_email = function (){
		alert('VINDO AQUI JÀ')
	}
});