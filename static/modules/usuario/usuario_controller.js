/**
 * Created by diego on 05/05/2017.
 */
var application = angular.module('modules.usuario', []);

application.controller('register_controller', function($scope) {

  $scope.save_user = function () {
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
});


application.controller('login_controller', function($scope) {

  $scope.login_autentication = function () {
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    NProgress.start();
    if (validate_form_login()){
      $.ajax({
        type: "POST",
        url: "/api/usuario/login/autentication",
        data: {
          email: $scope.email,
          senha: $scope.senha,
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
  }
});