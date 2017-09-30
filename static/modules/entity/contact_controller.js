application.controller('register_phone_entity', function ($scope) {
	$scope.contacts = [];
	$scope.contact_selected = null;
	$scope.changing_contact = false;
	$scope.entity_selected = null


	/*Quando o modal ficar off, limpamos os campos e as variaveis controladoras, remover class wrong_field*/
	$('#modal_add_phone').on('hidden.bs.modal', function () {
		$(this).find("input,textarea,select").val('').end();
		$scope.contact_selected.selected = ''
		$scope.changing_contact = false;
		$scope.contact_selected = null;
		clean_wrong_field('ddd')
		clean_wrong_field('phone')
	});

	/*Controller of contacts*/
	$scope.save_tel = function () {
		$scope.contact_selected = null;
		var id_entity = angular.element(document.getElementById('identification_controller')).scope().entity_selected.id;
		var data_paramters = {
			type_contact: $('#type_contact').val(),
			name: $('#name_contact').val(),
			ddd: $('#ddd').val(),
			phone: $('#phone_number').val(),
			complemento: $('#complemento').val(),
			id_entity: id_entity,
			type_class : 'Contact'
		};

		success_function = function () {
			//check_response_message_form('#form-save-contact',message)
			alert("Sucesso")
			notify('success','Contato Adicionado','Seu contato foi registrado')
			$scope.load_contacts()
			$('#modal_add_phone').modal('hide')

		}

		fail_function = function () {
			notify('error','Error ao tentar salvar','Não foi possivel salvar o contato')
		}
		request_api("/api/entity/register/contact/" + id_entity +"/", data_paramters, validate_contact, success_function, fail_function)
	};

	$scope.load_contacts = function () {
		$scope.entity_selected =  angular.element(document.getElementById('identification_controller')).scope().entity_selected;
		var id = $scope.entity_selected.id
		var type_class = 'Contact'
		$.ajax({
				type: 'GET',
				url: "/api/entity/list/contacts/" + id +'/' + type_class +'/',

				success: function (data) {
					$scope.contacts = JSON.parse(data)
					$scope.$apply();
				},

				failure: function (data) {
					alert("Não foi possivel carregar a lista")
			}
		})
		$scope.$apply();
	};

	$scope.delete_contact = function () {

		var contact_delete = $scope.contact_selected.id
		$.ajax({
			url: "/api/entity/delete/phone/" + contact_delete + "/Contact",
			success : function () {
				$scope.contact_selected = null
				$scope.load_contacts()
				notify('success','Contato Removido','Seu contato foi removido do sistema')
				$scope.$apply()
			},
		})
	};

	$scope.load_field_email = function () {
		alert("Vindo aqui, Falta fazer")
	}

	$scope.change_email = function () {
		alert("Vindo aqui, Falta fazer")
	}

	/**$scope.select_table_row_contact = function (contact) {
		if ($scope.contact_selected !== null) {
			if ($scope.contact_selected == contact) {
				$scope.unselect_table_row();
				$scope.$apply();
			}
			else {
				$scope.unselect_table_row();
				$scope.contact_selected = contact

				$("#table_contacts").children("tr").eq(contact).addClass('selected')
				$scope.$apply();

				//$scope.carregar_indicacao_selecionada();
			}
		}
		else {
			$("#table_contacts").children("tr").eq(contact).addClass('selected')
			$scope.contact_selected = contact;
			$scope.$apply();
			//$scope.carregar_indicacao_selecionada();
		}
	};

	$scope.unselect_table_row = function () {
		$("#table_contacts").children("tr").eq($scope.contact_selected).removeClass('selected')
		$scope.contact_selected = null
	};
	**/
	$scope.select_contact = function(contact){
    if ($scope.contact_selected !==  null){
      if($scope.contact_selected == contact){
        $scope.unselect_row_contact();
      }
      else{
        $scope.unselect_row_contact();
        $scope.select_row_contact(contact);
        //$scope.carregar_indicacao_selecionada();
      }
    }
    else{
      $scope.select_row_contact(contact);
    }
    $scope.$apply();
  }

  $scope.select_row_contact = function (contact) {
  	$scope.contact_selected = contact;
		$scope.contact_selected.selected = 'selected';
  }

  $scope.unselect_row_contact = function () {
		$scope.contact_selected.selected = '';
    $scope.contact_selected = null;
  }

	$scope.check_disable = function () {
		if ($scope.email_selected == null){
			return true
		}else{
			return false
		}
	};

	$scope.load_field_contact = function () {
		$scope.changing_contact = true
		$.ajax({
			type: 'GET',
			url: '/api/entity/fields/contacts/' + $scope.contact_selected.id,

			success: function (data) {
				data = JSON.parse(data)
				$('#modal_add_phone').modal()
				$('#type_contact').val(data.type_contact)
				$('#phone_number').val(data.phone)
				$('#ddd').val(data.ddd)
				$('#name_contact').val(data.name)
				$('#complemento').val(data.complemento)
				}
		})
	};

	$scope.change_contact = function () {

		/*Falta colocar um id para passar ao banco*/
		var cpf_cnpj = '14960175796';
		var data_paramters = {
			id : $scope.contact_selected.id,
			type_contact: $('#type_contact').val(),
			name: $('#name_contact').val(),
			ddd: $('#ddd').val(),
			phone: $('#phone_number').val(),
			complemento: $('#complemento').val(),
			id_entity: cpf_cnpj
		};

		/*Variaveis auxiliares usadas no if do modal*/
		var complemento = $scope.contact_selected.complemento;
		var complet_phone = '('+ data_paramters.ddd + ')' + data_paramters.phone;
		complemento === null? complemento='' : {} ;

		/*Verifica se o modal Alterar possui mudanças*/
		if (!($scope.contact_selected.name == data_paramters.name
				&& $scope.contact_selected.phone == complet_phone
				&& $scope.contact_selected.type_contact == data_paramters.type_contact
				&& ( data_paramters.complemento == complemento)
				))
			{
				success_function = function (message) {
					//check_response_message_form('#form-save-contact',message)
					$scope.load_contacts();
					$('#modal_add_phone').modal('hide');
					notify('success','Contato Alterado','Seu contato foi alterado')
				}

				fail_function = function () {
					alert("Deu Ruim Na alteração")
					$('#modal_add_phone').modal('hide');
				}
				request_api("/api/entity/update/phone", data_paramters, validate_contact, success_function, fail_function)
		}
		else
		{
			$('#modal_add_phone').modal('hide');
			notify('error','Sem alterações','Para salvar alterações, realize uma')
		}
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

application.controller('register_email_entity', function ($scope) {
	/*Variaveis*/
	$scope.emails = []
	$scope.email_selected = null
	$scope.changing_email = null
	$scope.entity_selected = null

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
