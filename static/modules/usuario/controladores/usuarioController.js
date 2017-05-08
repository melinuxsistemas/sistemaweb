/**
 * Created by diego on 05/05/2017.
 */

angular.module('modules.usuario', []).controller('controller_register', function($scope) {

  $scope.salvar_usuario = function (token) {
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    alert("token: "+csrftoken);
    NProgress.start();
    if (validar_formulario()){

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
          var resultado = response['success']
          var data_object = response['data-object']
          var message = response['message']

          alert("resultado: "+resultado+" - "+message)
          alert("Olha os dados: "+data_object)
          if (resultado == true) {
            success_notify("Usuário Cadastrado","Você receberá um email em instantes."+data_object)
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
