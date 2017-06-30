/**
 * Created by diego on 05/05/2017.
 */
var application = angular.module('modules.usuario', []);

application.controller('reset_password_controller', function($scope) {

  success_function = function(){
      confirm_notify("Operação realizada com Sucesso!","Verifique seu email, você receberá um email em instantes.<br><a href='/login'>Clique aqui para acessar sistema.</a>")
  }

  $scope.reset_password = function () {
    var data_paramters = {email: $scope.email}
    validate_form_reset_password()
    request_api("/api/usuario/reset_password",data_paramters,validate_form_reset_password,success_function,null)
  }

  $scope.resend_activation_code = function () {
    var data_paramters = {email: $scope.email}
    request_api("/api/usuario/reactivate",data_paramters,validate_form_reset_password,success_function,null)
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
      $scope.old_password = "";
      $scope.password = "";
      $scope.confirm_password = "";
    }

    //validate_form_change_password()

    request_api("/api/usuario/change_password",data_paramters,validate_form_change_password,success_function,null)
  }
});

application.controller('register_controller', function($scope) {

  $scope.email = "";
  $scope.password = "";
  $scope.confirm_password = "";

  $scope.save_user = function () {
    var data_paramters = {
      email: $scope.email,
      password: $scope.password,
      confirm_password: $scope.confirm_password,
    }
    success_function = function(){
      window.location = "/register/confirm/"+$scope.email;
    }
    request_api("/api/usuario/register/save",data_paramters,validate_form_register,success_function,null)
  }

  $scope.resend_activation_code = function () {
    var data_paramters = {email: $scope.email}
    $("#email").val($scope.email)
    success_function = function(){
      confirm_notify("Operação realizada com Sucesso!","Verifique seu email, você receberá um email em instantes.<br><a href='/login'>Clique aqui para acessar sistema.</a>")
    }
    request_api("/api/usuario/reactivate",data_paramters,validate_form_confirm_register,success_function,null)
  }
});

application.controller('login_controller', function($scope) {

  $scope.login_autentication = function () {
    var data_paramters = {email: $scope.email, password: $scope.password}
    success_function = function(){
      window.location = "/";
    }
    request_api("/api/usuario/login/autentication",data_paramters,validate_form_login,success_function,null)
  }
});
