alert("Carreguei o controller do contatos")
application.controller('register_phone_entity', function ($scope) {
	$scope.contacts = []
	$scope.contact_selected = null

	/*Controller of contacts*/
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
			$scope.load_contacts()
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

	$scope.select_table_row_contact = function (contact) {
		alert("Entrando aqui!!" + JSON.stringify(contact))

		if ($scope.contact_selected !== null) {
			if ($scope.contact_selected == contact) {
				alert("Contato iguais eu removo seleção")
				$scope.unselect_table_row();
				$scope.$apply();
			}
			else {
				alert("Primeiro desmarco, para selecionar outro")
				$scope.unselect_table_row();
				alert("Consigo sair?")
				$scope.contact_selected = contact

				$("#table_contacts").children("tr").eq(contact).addClass('selected')
				$scope.$apply();

				//$scope.carregar_indicacao_selecionada();
			}
		}
		else {
			alert("Selecionando uma linha")
			$("#table_contacts").children("tr").eq(contact).addClass('selected')
			$scope.contact_selected = contact;
			$scope.$apply();
			//$scope.carregar_indicacao_selecionada();
		}
	}

	$scope.unselect_table_row = function () {
		$("#table_contacts").children("tr").eq($scope.contact_selected).removeClass('selected')
		$scope.contact_selected = null
	}

});

application.controller('register_entity_email', function ($scope) {
	alert("cheguei no controller do email agora")
	/*Variaveis*/
	$scope.emails = []
	$scope.teste = 'BEM VINDO AO CONTROLLER EMAIL'
	$scope.email_selected = null

	$scope.save_email = function () {
		var data_paramters = {
			email : $('#email').val(),
			name : $('#name').val(),
			send_xml : $('#send_xml').val(),
			send_suitcase : $('#send_suitcase').val()
		}

		alert("OLHA O DICT"+JSON.stringify(data_paramters))


		sucess_function = function () {
			alert("Já salvei")
		}


		fail_function = function () {
			alert("Não foi dessa vez")
		}
		request_api("/api/entity/register/email", data_paramters, validate_email, sucess_function, fail_function)

	}


	$scope.load_emails = function () {
		//$.ajax()
	}

	$scope.select_table_row_email = function (email) {
		alert("Vindo aqui no select")
	}
});
