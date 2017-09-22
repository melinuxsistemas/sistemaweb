/**
 * Created by diego on 05/05/2017.
 */
var application = angular.module('modules.entity', []);
application.controller('register_controller', function($scope) {

	$scope.minimal_quantity_rows = [0,1,2,3,4,5,6,7,8,9,0];
	$scope.entity_test = [1]
  $scope.entity_selected = null
  $scope.list_entities = ['iniciar lista']

  $scope.load_table_entity = function () {
    $.ajax({
      type: 'GET',
      url: "/api/entity/load_entities/",

      success: function (data) {
        $scope.list_entities = JSON.parse(data)
        $scope.$apply();
      },

      failure: function (data) {
        alert("Não foi possivel carregar a lista")
      },
    })
}

  $scope.select_table_row = function(entity){
	   alert("Entrando aqui!!"+JSON.stringify(entity))

    if ($scope.entity_selected !==  null){
      if($scope.entity_selected == entity){
        alert("Entity iguais eu removo seleção")
        $scope.unselect_table_row();
        $scope.$apply();
      }
      else{
        alert("Primeiro desmarco, para selecionar outro")
        $scope.unselect_table_row();
        alert("Consigo sair?")
        $scope.entity_selected = entity

        $("#table_entity").children("tr").eq(entity).addClass('selected')
        $scope.$apply();

        //$scope.carregar_indicacao_selecionada();
      }
    }
    else{
      alert("Selecionando uma linha")
      $("#table_entity").children("tr").eq(entity).addClass('selected')
      $scope.entity_selected = entity;
      $scope.$apply();
      //$scope.carregar_indicacao_selecionada();
    }

  }

  $scope.unselect_table_row = function () {
    $("#table_entity").children("tr").eq($scope.entity_selected).removeClass('selected')
    $scope.entity_selected = null
  }
});

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



