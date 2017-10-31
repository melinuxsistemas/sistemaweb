/**
 * Created by diego on 05/05/2017.
 */
var application = angular.module('modules.entity', ['angularUtils.directives.dirPagination']);
application.controller('identification_controller', function($scope) {

	$scope.screen_height = SCREEN_PARAMTERS['screen_height']
	$scope.screen_width  = SCREEN_PARAMTERS['screen_width']
	$scope.screen_model  = SCREEN_PARAMTERS['screen_model']

	$scope.table_maximun_items_per_page = SCREEN_PARAMTERS['table_maximun_items_per_page']
	$scope.table_minimun_items          = SCREEN_PARAMTERS['table_minimun_items']
	$scope.table_maximun_body_height    = SCREEN_PARAMTERS['table_maximun_body_height']
	//alert("veja o tamanho: "+$scope.table_maximun_body_height)


	$scope.sortType           = 'entity_code';    // set the default sort type
	$scope.sortReverse        = false;            // set the default sort order
	$scope.search             = '';              // set the default search/filter term
	$scope.filter_by          = '1';
	$scope.filter_by_index    = parseInt($scope.filter_by);
	$scope.filter_by_options  = ["entity_code","entity_name", "cpf_cnpj"];

	$scope.loaded_entities = false;
  $scope.entity_selected = null
  $scope.list_entities = []

  $scope.save = function () {
  	alert("TO SALVANDO A IDENTIFICACAO DE UMA ENTIDADE")

  	var fields = {};
		$.each($('#form-save-entity').serializeArray(), function(i, field) {
			//alert("VEJA I: "+i+" - Field: "+field.name+" - Value: "+field.value)
				fields[field.name] = field.value;
		});
		//$('#form-save-entity').serialize();
  	//alert("VEJA OS VALORES: "+JSON.stringify(fields))

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

    success_function = function(result,message,object,status){
      //window.location = "/"//register/confirm/"+$scope.email;
      if(result == true){
      	check_response_message_form('#form-save-entity', message);
				//$scope.list_entities.push(object)
				$scope.list_entities.splice(0, 0, object);
				$scope.$apply();
				document.getElementById("form-save-entity").reset();
				$("#modal_identification").modal('hide');
      }
		}

    fail_function = function (result,message,data_object,status) {
      check_response_message_form('#form-save-entity', message);
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

        $scope.list_entities = JSON.parse(data);
        $("#loading_tbody").fadeOut();
        $scope.$apply();
        $scope.loaded_entities = true;
        $scope.$apply();
      },

      failure: function (data) {
        $scope.loaded_entities = true;
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



	$scope.readjust_screen = function (){
		//alert("ACIONEI O CONTROLE DO ANGULAR PRA VERIFICAR OS PARAMETROS")
		$scope.screen_height = SCREEN_PARAMTERS['screen_height']
		$scope.screen_width  = SCREEN_PARAMTERS['screen_width']
		$scope.screen_model  = SCREEN_PARAMTERS['screen_model']

		$scope.table_maximun_items_per_page = SCREEN_PARAMTERS['table_maximun_items_per_page']
		$scope.table_minimun_items          = SCREEN_PARAMTERS['table_minimun_items']
		$scope.table_maximun_body_heigth    = SCREEN_PARAMTERS['table_maximun_body_heigth']
		$scope.$apply();
	}
});

/*
application.controller('register_person_controller', function($scope) {
  $scope.cpf_cnpj = "";
  $scope.entity_name = "";
  $scope.fantasy_name = "";
  $scope.confirm_password = "";
  $scope.birth_date_foundation = "";
  $scope.teste = "TESTE"

  $scope.save_person = function () {
  	alert("EH NESSE CARA AQUI QUE TO TENTANDO SALVAR ALGUEM")
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
*/

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



