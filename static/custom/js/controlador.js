 var app = angular.module('NovaApp', []);
 var esta_adicionando = null;
 var tipo_operacao = null


 app.controller('MeuController', function($scope) {
    $scope.tipo_operacao = null;
    $scope.esta_adicionando = true;
    $scope.registro_selecionado = null;

    $scope.registro_marcado = "desabilitado";

    $scope.incluir_usuario = function() {
        var email= $scope.email;
        var senha = $scope.senha;
        alert('Vai incluir usuario '+email);
        if(email){
            $.ajax({
                type: "POST",
                url: "/usuario/grava_novo/",
                data: {
                    email: email,
                    senha: senha,
                    csrfmiddlewaretoken: '{{ csrf_token }}'
                },

                success: function (data) {
                    var resultado = $.parseJSON(data);
                    if (resultado['success'] == true){
                        parametro = resultado["message"].split("#")
                        var usuario = {
                            email : email,
                            senha: senha
                        };

                        $scope.$apply();
                    }

                    else{
                        alert(resultado["message"]);
                    }
                },
                failure: function (data) {
                    alert('Erro! Falha na execução do ajax');
                }
            });
        }
        else{
            alert('Erro! Preencha os campos antes de enviar');
        }

        //e.preventDefault();
    }

    $scope.alterar_usuario = function() {
        var email = $scope.email;
        var senha = $scope.senha;

        if(email){
           if (confirm('Confirma alteraçoes desse Usuario?')) {
              $.ajax({
                    type: "POST",
                    url: "/alterar/" + $scope.registro_selecionado.id + "/",
                    data: {
                        email: email,
                        senha: senha,
                        csrfmiddlewaretoken: '{{ csrf_token }}'

                    },
                    success: function (data) {
                        var resultado = $.parseJSON(data);
                        if (resultado['success'] == true) {
                            $scope.registro_selecionado.email = email;
                            $scope.registro_selecionado.senha = senha;
                            $scope.resetar_formulario_usuario();
                            $scope.$apply();

                        }

                        else {
                            alert(resultado["message"]);
                        }

                    },
                    failure: function (data) {
                        alert('Erro! Falha na execução do ajax');
                    }

              });


           } else {
              //e.preventDefault();
           }

        }
        else{
            alert('Erro! Preencha os campos antes de enviar');
        }

        //e.preventDefault();

    }

    $scope.configurar_incluir_usuario = function(){

        $scope.esta_adicionando = true;
        $scope.email = "";
        $scope.senha = "";
    }

    $scope.configurar_alterar_usuario = function(){

        $scope.esta_adicionando = false;
        $scope.email = $scope.registro_selecionado.email;
        $scope.senha = $scope.registro_selecionado.senha;

    }

    $scope.resetar_formulario_usuario = function(){

        $scope.email.val("");
        $scope.senha.val("");
        $scope.registro_marcado = "desabilitado";
    }

});






