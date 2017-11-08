/**
 * Created by diego on 05/05/2017.
 */
var application = angular.module('modules.usuario', []);

application.controller('reset_password_controller', function($scope) {

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
    request_api("/api/user/register/save",data_paramters,validate_form_register,success_function,null)
  }

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

  	SESSION_PARAMTERS['email'] = $scope.email
  	SESSION_PARAMTERS['password'] = $scope.password

    var data_paramters = SESSION_PARAMTERS//{email: $scope.email, password: $scope.password}

    function success_function(result,message,data_object,status){
    	//check_response_message_form('#form_login', message);
    	//alert("VEJA O QUE VEIO: "+result+" - "+message+" - "+data_object+" - "+status)
    	//notify_response_message(message)
    	alert("deu certo")
    	var redirect = "/"
    	return redirect
    }

    fail_function = function (result,message,data_object,status) {
    	alert("FALHA: "+result+" - "+message+" - "+data_object+" - "+status)
      notify_response_message(message);
    }

    request_api("/api/user/login/autentication",data_paramters,validate_form_login,success_function,fail_function)
  }
});