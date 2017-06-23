/**
 * Created by diego on 05/05/2017.
 */
var application = angular.module('modules.usuario', []);

application.controller('reset_password_controller', function($scope) {

  var data_paramters = {email: $scope.email}
  success_function = function(){
      confirm_notify("Operação realizada com Sucesso!","Verifique seu email, você receberá um email em instantes.<br><a href='/login'>Clique aqui para acessar sistema.</a>")
  }

  $scope.reset_password = function () {
    request_api("/api/usuario/reset_password",data_paramters,validate_form_reset_password,success_function,null)
  }

  $scope.resend_activation_code = function () {
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

    request_api("/api/usuario/change_password",data_paramters,validate_form_change_password,null,null)
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

  /*$scope.save_users = function () {
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    NProgress.start();
    if (validate_form_register()){
      $.ajax({
        type: "POST",
        url: "/api/usuario/register/save",
        data: {
          email: $scope.email,
          senha: $scope.senha,
          confirma_senha: $scope.confirma_senha,
          csrfmiddlewaretoken: csrftoken
        },

        success: function (data) {
          var response = $.parseJSON(data);
          var message = response['message']
          var resultado = response['success']
          if (resultado == true) {
            var data_object = $.parseJSON(response['data-object'])
            var moment_date = moment(data_object['fields']['joined_date']).format("DD/MM/YYYY - HH:mm:ss")
            success_notify("Usuário Cadastrado","Você receberá um email em instantes. \n<sub>"+moment_date+"</sub>")
          }

          else {
            alert("MENSAGEM "+message)
            error_notify('email',"Falha na operação",message)
          }
        },
        failure: function (data) {
          error_notify('email',"Falha na operação","Erro na requisição ao servidor.")
        }
      });

      NProgress.done();
      return true;
    }
    else{
      NProgress.done();
      return false;
    }
  }
  */
});

application.controller('login_controller', function($scope) {

  $scope.login_autentication = function () {
    var data_paramters = {email: $scope.email, password: $scope.password}
    success_function = function(){
      window.location = "/";
    }
    request_api("/api/usuario/login/autentication",data_paramters,validate_form_login,success_function,null)

    /*
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    NProgress.start();
    if (validate_form_login()){
      $.ajax({
        type: "POST",
        url: "/api/usuario/login/autentication",
        data: {
          email: $scope.email,
          password: $scope.password,
          csrfmiddlewaretoken: csrftoken
        },

        success: function (data) {
          var response = $.parseJSON(data);
          var message = response['message']
          var resultado = response['success']
          if (resultado == true) {
            var data_object = $.parseJSON(response['data-object'])
            //alert("Veja o model: "+data_object['fields']['joined_date'])
            NProgress.done();
            window.location.replace("/");
          }
          else {
            error_notify('email',"Falha na operação",message)
          }
        },
        failure: function (data) {
          NProgress.done();
          error_notify('email',"Falha na operação","Erro na requisição ao servidor.")
        }
      });

      NProgress.done();
      return true;
    }
    else{
      NProgress.done();
      return false;
    }
  */
  }
});
