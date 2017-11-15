/**
 * Created by diego on 05/05/2017.
 */
var application = angular.module('modules.user', []);

application.controller('reset_password_controller', function($scope) {

  $scope.reset_password = function () {
  	var data_paramters = {email: $scope.email}

  	var success_function = function success_function(result,message,data_object,status){
			success_notify("Operação realizada com Sucesso!","Verifique seu email, você receberá um email em instantes.")
    }

    var fail_function = function (result,message,data_object,status) {
      notify_response_message(message);
    }

    validate_function = function(){
			return email_is_valid("email")
		}
    request_api("/api/user/reset_password",data_paramters,validate_function,success_function,fail_function)
  }

  $scope.resend_activation_code = function () {
    var data_paramters = {email: $scope.email}

    var success_function = function success_function(result,message,data_object,status){
			success_notify("Operação realizada com Sucesso!","Verifique seu email, você receberá um email em instantes.")
    }

    var fail_function = function (result,message,data_object,status) {
    	notify_response_message(message);
    }

    validate_function = function(){
			return email_is_valid("email")
		}
    request_api("/api/user/reactivate",data_paramters,validate_function,success_function,fail_function)
  }
});

application.controller('change_password_controller', function($scope) {

  $scope.save_password = function () {
    var data_paramters = {
      old_password: $scope.old_password,
      password:  $scope.password,
      confirm_password:  $scope.confirm_password
    }

    success_function = function(result,message,data_object,status){
    	success_notify("Operação realizada com Sucesso!","Senha de acesso redefinida.")
      $("#old_password").val("")
      $("#password").val("")
      $("#confirm_password").val("")
      $scope.old_password = "";
      $scope.password = "";
      $scope.confirm_password = "";
    }

    fail_function = function (result,message,data_object,status) {
      notify_response_message(message);
    }

    request_api("/api/user/change_password",data_paramters,validate_form_change_password,success_function,fail_function)
  }
});

application.controller('register_controller', function($scope) {

  $scope.email = "";
  $scope.password = "";
  $scope.confirm_password = "";

  $scope.save_user = function () {

		var data_paramters = {};
  	$.each($('#form_register').serializeArray(), function(i, field) {
			data_paramters[field.name] = field.value;
		});

    success_function = function(result,message,data_object,status){
    	var redirect = "/register/confirm/"+$scope.email;
    	return redirect
    }

    fail_function = function (result,message,data_object,status) {
      notify_response_message(message);
    }
    request_api("/api/user/register/save",data_paramters,validate_form_register,success_function,fail_function)
  }

  $scope.resend_activation_code = function () {
  	var data_paramters = {email: $scope.email}

    var success_function = function success_function(result,message,data_object,status){
			success_notify("Operação realizada com Sucesso!","Verifique seu email, você receberá um email em instantes. <br><a href='/login'>Clique aqui para acessar sistema.</a>")
    }

    var fail_function = function (result,message,data_object,status) {
    	notify_response_message(message);
    }

    validate_function = function(){
    	return true;
		}

		alert("veja eh isso")
    request_api("/api/user/reactivate",data_paramters,validate_function,success_function,fail_function)
  }
});

application.controller('login_controller', function($scope) {

  $scope.login_autentication = function () {

  	SESSION_PARAMTERS['email'] = $scope.email
  	SESSION_PARAMTERS['password'] = $scope.password

    var data_paramters = SESSION_PARAMTERS//{email: $scope.email, password: $scope.password}

    function success_function(result,message,data_object,status){
    	//alert("VEJA O QUE VEIO: "+result+" - "+message+" - "+data_object+" - "+status.request_path)

    	var redirect = "/"
    	return redirect
    }

    fail_function = function (result,message,data_object,status) {
    	//alert("FALHA: "+result+" - "+message+" - "+data_object+" - "+status)
      notify_response_message(message);
    }

    request_api("/api/user/login/autentication",data_paramters,validate_form_login,success_function,fail_function)
  }
});

application.controller('users_controller', function($scope) {
	$scope.list_users = [];
	$scope.table_minimun_items_u = [1,1,1,1,1,1,1];
	$scope.loaded_entities = false;
	$scope.user_selected = null;


  $scope.filter_users = function(){
  	$.ajax({
      type: 'GET',
      url: "/api/user/users/filter",

      success: function (data) {
				data = JSON.parse(data);
				$scope.list_users = data['object'];
        $("#loading_tbody").fadeOut();
        $scope.loaded_entities = true;
        $scope.$apply();
      },

      failure: function (data) {
        $scope.loaded_entities = true;
        alert("Não foi possivel carregar a lista")
      }
    })
	}

	$scope.select_user = function(user){
    if ($scope.user_selected !==  null){
      if($scope.user_selected == user){
        $scope.unselect_row();
      }
      else{
        $scope.unselect_row();
        $scope.select_row(user);
      }
    }
    else{
      $scope.select_row(user);
    }
    $scope.$apply();
  }

  $scope.select_row = function (user) {
  	$scope.user_selected = user;
		$scope.user_selected.selected = 'selected';
  }

  $scope.unselect_row = function () {
		$scope.user_selected.selected = '';
    $scope.user_selected = null;
  }
});


