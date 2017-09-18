application.controller('register_phone_entity', function ($scope) {
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

		alert('Vindo')
		$scope.contacts = []
		$.ajax({

			type: 'GET',
			url: "/api/entity/contacts/" + '14960175796',//$scope.registro_selecionado.cliente_id,

			success: function (data) {
				alert("Consegui");
				$scope.contacts = JSON.parse(data);
				$scope.$apply();
				//alert("VEJA O QUE TEMOS NAS INDICACOES: "+$scope.registro_selecionado.indicacoes[0].cliente_id)
			},

			failure: function (data) {
				$scope.clientes = [];
				$scope.desabilitar = 'link_desabilitado'
				alert("Não foi possivel carregar a lista de indicacoes")
			}

		})}


});
