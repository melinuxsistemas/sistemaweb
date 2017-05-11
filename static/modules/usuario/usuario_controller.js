/**
 * Created by diego on 05/05/2017.
 */

angular.module('modules.usuario', []).controller('register_controller', function($scope) {

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

angular.module('modules.usuario', []).controller('login_controller', function($scope) {

  $scope.logar_usuario = function () {
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    NProgress.start();
    alert("Vai validar email "+$scope.email);
    //if (validate_form_login()){

      $.ajax({
        type: "POST",
        url: "/api/usuario/login/save",
        data: {
          email: $scope.email,
          senha: $scope.senha,
          csrfmiddlewaretoken: csrftoken
        },

        success: function (data) {
          alert(data);
          var response = $.parseJSON(data);
          var message = response['message']
          var resultado = response['success']
          if (resultado == true) {
            var data_object = $.parseJSON(response['data-object'])
            //alert("Veja o model: "+data_object['fields']['joined_date'])
            alert("Usuario logado")
            //success_notify("Usuário Cadastrado","Você receberá um email em instantes. \n<sub>"+moment_date+"</sub>")
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
    //}
    //else{
    //  NProgress.done();
    //  return false;
    //}
  }
});
