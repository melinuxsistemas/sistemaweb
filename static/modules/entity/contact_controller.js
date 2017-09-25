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
			operadora: $('#complemento').val(),
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
			url: "/api/entity/list/contacts/" + '14960175796/',

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

		var contact_delete = $scope.contact_selected.id
		$.ajax({
			url: "/api/entity/delete/phone/" + contact_delete.toString(),
			success : function () {
				$scope.contact_selected = null
				$scope.load_contacts()
				$scope.$apply()
			},
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

	$scope.check_disable = function () {
		if ($scope.email_selected == null){
			return true
		}else{
			return false
		}
	}
});

application.controller('register_email_entity', function ($scope) {
	/*Variaveis*/
	$scope.emails = []
	$scope.email_selected = null

	$scope.save_email = function () {
		var data_paramters = {
			email : $('#email').val(),
			name : $('#name').val(),
			send_xml : $('#send_xml').val(),
			send_suitcase : $('#send_suitcase').val()
		}

		sucess_function = function () {
			$scope.load_emails()
			$('#modal_add_email').modal('hide')

		}

		fail_function = function () {
			alert("Email já cadasrasdo!\nInforme outro endereço de email")
		}
		request_api("/api/entity/register/email", data_paramters, validate_email, sucess_function, fail_function)

	}

	$scope.load_emails = function () {
		$.ajax({
			//Por hora a tabela esta fixa
			type: "GET",
			url: "/api/entity/list/emails/" + "14960175796/",

			success: function (data) {
				$scope.emails = JSON.parse(data)
				$scope.$apply()
			},

			failure : function (data) {
				alert("Não foi possível carregar a lista")
			}

		})
	}

	$scope.select_table_row_email = function (email) {

		alert(JSON.stringify($scope.email_selected))
		if ($scope.email_selected !== null) {
			if ($scope.email_selected == email) {
				alert("emails iguais eu removo seleção")
				$scope.unselect_table_row_email();
				$scope.$apply();
			}
			else {
				alert("Primeiro desmarco, para selecionar outro")
				$scope.unselect_table_row_email();
				$scope.email_selected = email
				//alert(JSON.stringify($scope.email_selected.$$hashKey))
				alert(JSON.stringify($scope.email_selected.id))
				$("#table_emails").children("tr").eq(email).addClass('selected')
				$scope.$apply();
				//$scope.carregar_indicacao_selecionada();
			}
		}
		else {
			alert("Selecionando uma linha")
			$("#table_emails").children("tr").eq(email).addClass('selected')
			$scope.email_selected = email;
			$scope.$apply();
		}
	}

	$scope.unselect_table_row_email = function () {
		$("#table_emails").children("tr").eq($scope.email_selected).removeClass('selected')
		$scope.email_selected = null
		}

	$scope.delete_email = function () {
		var email_delete = $scope.email_selected.id
		alert('olha o email')
	}
});
