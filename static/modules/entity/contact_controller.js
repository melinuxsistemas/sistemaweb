application.controller('register_phone_entity', function ($scope) {
	$scope.contacts = []
	$scope.contact_selected = null

	$scope.save_tel = function () {
		alert("Entrando no controlador")
		//var cpf_cnpj = $('#cpf_cnpj').val();
		var cpf_cnpj = '14960175796';
		var data_paramters = {
			type_contact: $('#type_contact').val(),
			name: $('#name_contact').val(),
			ddd: $('#ddd').val(),
			phone: $('#phone_number').val(),
			operadora: $('#operadora').val(),
			id_entity: cpf_cnpj
		}

		success_function = function (message) {
			//check_response_message_form('#form-save-contact',message)
			alert("Salvou")
			$scope.reset_form()
			$('#modal_add_phone').modal('hide')

		}

		fail_function = function () {
			alert("Deu Ruim")
		}
		request_api("/api/entity/register/phone", data_paramters, validate_contact, success_function, fail_function)
	}

	$scope.reset_form = function () {
		document.getElementById("form-save-contact").reset();
	}

	$scope.load_contacts = function () {
		$.ajax({
			type: 'GET',
			url: "/api/entity/contacts/" + '14960175796',

			success: function (data) {
				$scope.contacts = JSON.parse(data)
				$scope.$apply();
			},

			failure: function (data) {
				alert("Não foi possivel carregar a lista")
			},
		})
	}

	$scope.delete_contact = function () {
		$.ajax({
			url: "/api/entity/delete/phone/" + '17',
		})
	}

	$scope.selecionar_linha = function(contact){
	    alert("Entrando aqui!!"+contact)
			if ($scope.contact_selected !==  null){
				if($scope.contact_selected == contact){
				  alert("Entity iguais eu removo seleção")
					$scope.desmarcar_linha_indicacao();
					$scope.$apply();
				}
				else{
				  alert("Primeiro desmarco, para selecionar outro")
					$scope.desmarcar_linha_indicacao();
					contact.selected = 'selected';
					$scope.contact_selected = contact
					$scope.$apply();
					//$scope.carregar_indicacao_selecionada();
				}
			}
			else{
				contact.selected = 'selected';
				$scope.contact_selected = contact;
				$scope.$apply();
			}

		}

	$scope.desmarcar_linha_indicacao = function () {
      $scope.contact.selected = ''
      $scope.contact_selected = null
		}
});
