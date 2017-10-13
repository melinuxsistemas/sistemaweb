/**
 * Created by diego on 05/05/2017.
 */
var application = angular.module('modules.entity', ['angularUtils.directives.dirPagination']);
application.controller('identification_controller', function($scope) {

	$scope.sortType           = 'entity_code';    // set the default sort type
	$scope.sortReverse        = false;  // set the default sort order
	$scope.filter_by          = '1';
	$scope.filter_by_index    = parseInt($scope.filter_by);
	$scope.filter_by_options  = ["entity_code","entity_name", "cpf_cnpj"];
	$scope.search             = '';     // set the default search/filter term

	$scope.minimal_quantity_rows = [0,1,2,3,4,5,6,7,8,9];
  $scope.entity_selected = null
  $scope.list_entities = []

  $scope.save = function () {

    $scope.cpf_cnpj = $('#cpf_cnpj').val();
    $scope.birth_date_foundation = $('#birth_date_foundation').val();

    var data_paramters = {
      entity_type: 'PF',
      registration_status: 0,
      cpf_cnpj: clear_mask_numbers($scope.cpf_cnpj),
      entity_name: $('#entity_name').val().toUpperCase(),
      fantasy_name: $('#fantasy_name').val().toUpperCase(),
      birth_date_foundation: $scope.birth_date_foundation,
      comments: $scope.comments
    }

    success_function = function(result,message,object){

      //window.location = "/"//register/confirm/"+$scope.email;
      if(result == true){
      	alert("Vindo")
      	check_response_message_form('#form-save-entity', message);
				//$scope.list_entities.push(object)
				$scope.list_entities.splice(0, 0, object);
				$scope.$apply();
				document.getElementById("form-save-entity").reset();
				$("#modal_identification").modal('hide');
      }
		}

    fail_function = function (message) {
      alert("Nao deu")
      check_response_message_form('#form-save-entity', message);
      //notify('error','Formulário com dados inválidos',message.cpf_cnpj)
    }

    validade_function = function () {
     return  true;//validate_form_regiter_person(); //validate_date($scope.birth_date_foundation);
    }
    request_api("/api/entity/register/person/save",data_paramters,validade_function,success_function,fail_function)
  }

  $scope.load_entities = function () {
    $.ajax({
      type: 'GET',
      url: "/api/entity/list/entities/",

      success: function (data) {
        $scope.list_entities = JSON.parse(data)
        $scope.$apply();
      },

      failure: function (data) {
        alert("Não foi possivel carregar a lista")
      },
    })
	}

	$scope.select_filter_by = function (index) {
		$scope.filter_by_index = parseInt($scope.filter_by);
		$scope.apply();
	}

	$scope.get_filter_column = function(){
			var filter_search_by = $scope.filter_by_options[$scope.filter_by_index];
			switch (filter_search_by) {
					case 'entity_code':
							//alert("filtrar por entity_code");
							return {id: $scope.search};
					case 'cpf_cnpj':
							//alert("filtrar pelo cpf ou cnpj");
							return {cpf_cnpj: $scope.search};
					default:
							return {entity_name: $scope.search}
			}
	}

  $scope.select = function(entity){
	   //alert("Entrando aqui!!"+JSON.stringify(entity))
    if ($scope.entity_selected !==  null){
      if($scope.entity_selected == entity){
        $scope.unselect_row();
      }
      else{
        $scope.unselect_row();
        $scope.select_row(entity);
        //$scope.carregar_indicacao_selecionada();
      }
    }
    else{
      $scope.select_row(entity);
      //angular.element(document.getElementById('controler_contact')).scope().load_contacts();
    }
    $scope.$apply();
  }

  $scope.select_row = function (entity) {
  	$scope.entity_selected = entity;
		$scope.entity_selected.selected = 'selected';
  }

  $scope.unselect_row = function () {
		$scope.entity_selected.selected = '';
    $scope.entity_selected = null;
  }

  $scope.S9 = false;  // Giant Screen:   1921 or more
	$scope.S8 = false;  // Larger Screen:  1680 ~ 1920
	$scope.S7 = false;  // Giant Screen:   1367 ~ 1680
	$scope.S6 = false;  // Larger Screen:  1025 ~ 1366
	$scope.S5 = false;  // Giant Screen:    801 ~ 1024
	$scope.S4 = false;  // Larger Screen:   641 ~ 800
	$scope.S3 = false;  // Large Screen:    481 ~ 640
	$scope.S2 = false;  // Medium Screen:   321 ~ 480
	$scope.S1 = false;  // Small Screen:    241 ~ 320
	$scope.S0 = false;  // Smaller Screen:    0 ~ 240


	$scope.readjust_screen = function (){
		$scope.screen_height = window.innerHeight
		$scope.screen_width  = window.innerWidth
		$scope.S9 = false;  // Giant Screen:   1921 or more
		$scope.S8 = false;  // Larger Screen:  1680 ~ 1920
		$scope.S7 = false;  // Giant Screen:   1367 ~ 1680
		$scope.S6 = false;  // Larger Screen:  1025 ~ 1366
		$scope.S5 = false;  // Giant Screen:    801 ~ 1024
		$scope.S4 = false;  // Larger Screen:   641 ~ 800
		$scope.S3 = false;  // Large Screen:    481 ~ 640
		$scope.S2 = false;  // Medium Screen:   321 ~ 480
		$scope.S1 = false;  // Small Screen:    241 ~ 320
		$scope.S0 = false;  // Smaller Screen:    0 ~ 240

		if ($scope.screen_width <= 240){ $scope.S0 = true; }
		else if ($scope.screen_width <= 320){ $scope.S1 = true; }
		else if ($scope.screen_width <= 480){ $scope.S2 = true;	}
		else if ($scope.screen_width <= 640){ $scope.S3 = true; }
		else if ($scope.screen_width <= 800){ $scope.S4 = true; }
		else if ($scope.screen_width <= 1024){ $scope.S5 = true; }
		else if ($scope.screen_width <= 1366){ $scope.S6 = true; }
		else if ($scope.screen_width <= 1680){ $scope.S7 = true; }
		else if ($scope.screen_width <= 1920){ $scope.S8 = true; }
		else{ $scope.S9 = true; }
		$scope.$apply();
	}
});

application.controller('register_person_controller', function($scope) {
  $scope.cpf_cnpj = "";
  $scope.entity_name = "";
  $scope.fantasy_name = "";
  $scope.confirm_password = "";
  $scope.birth_date_foundation = "";
  $scope.teste = "TESTE"

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
      alert(" deu")
      //window.location = "/"//register/confirm/"+$scope.email;
      check_response_message_form('#form-save-entity', message);
		}
    
    fail_function = function (message) {
      alert("Nao deu")
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



