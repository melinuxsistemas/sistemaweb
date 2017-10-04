application.controller('register_phone_entity', function ($scope) {
	$scope.contacts = [];
	$scope.contact_selected = null;
	$scope.changing_contact = false;
	$scope.entity_selected = null;


	/*Quando o modal ficar off, limpamos os campos e as variaveis controladoras, remover class wrong_field*/
	$('#modal_add_phone').on('hidden.bs.modal', function () {
		$(this).find("input,textarea,select").val('').end();
		$scope.contact_selected.selected = ''
		$scope.changing_contact = false;
		$scope.contact_selected = null;
		clean_wrong_field('ddd')
		clean_wrong_field('phone')
		$scope.$apply()
	});

	/*RESETAR DADOS PARA TRATAR A TROCA DE CONTATOS SEM ABRIR MODAL*/
	$scope.reset_contact = function () {
		$scope.contacts = [];
		$scope.contact_selected = null;
		$scope.changing_contact = false;
		$scope.entity_selected = null
	}
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

		success_function = function (result,message,data_object) {
			notify('success','Contato Adicionado','Seu contato foi registrado');
			var new_contact = data_object;
			$scope.contacts.push(new_contact);
			$scope.$apply()
			$('#modal_add_phone').modal('hide')

		}

		fail_function = function (message) {
			alert("Olha os errors:	"+JSON.stringify(message))
			notify('error','Error ao tentar salvar','Não foi possivel salvar o contato')
		}
		request_api("/api/entity/register/contact/" + id_entity +"/", data_paramters, validate_contact, success_function, fail_function)
	};

	$scope.load_contacts = function () {
		$scope.reset_contact();
		$scope.entity_selected =  angular.element(document.getElementById('identification_controller')).scope().entity_selected;
		var id = $scope.entity_selected.id
		$.ajax({
				type: 'GET',
				url: "/api/entity/list/contacts/" + id +'/',

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

		var id_contact = $scope.contact_selected.id
		$.ajax({
			url: "/api/entity/delete/phone/" + id_contact ,

			success : function () {
				$scope.contact_selected = null
				$scope.load_contacts()
				notify('success','Contato Removido','Seu contato foi removido do sistema')
				$scope.$apply()
			},
		})
	};

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
		$scope.changing_contact = true;
		$('#type_contact').val($scope.contact_selected.type_contact)
		$('#phone_number').val($scope.contact_selected.phone);
		$('#ddd').val($scope.contact_selected.ddd);
		$('#name_contact').val($scope.contact_selected.name)
		$('#complemento').val($scope.contact_selected.complemento)
	};

	$scope.change_contact = function () {
		alert("Vindo aqui?")

		var data_paramters = {
			id : $scope.contact_selected.id,
			type_contact: $('#type_contact').val(),
			name: $('#name_contact').val(),
			ddd: $('#ddd').val(),
			phone: $('#phone_number').val(),
			complemento: $('#complemento').val()
		};

		/*Verifica se o modal Alterar possui mudanças*/
		if ($scope.equals_fields_contact(data_paramters)) {
				alert("Entrando pra trocar")
				success_function = function (message) {
					alert("Sucesso")
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
			print("SIDJAIDJAI")
			$('#modal_add_phone').modal('hide');
			notify('error','Sem alterações','Para salvar alterações, realize uma')
		}
	}

	$scope.equals_fields_contact = function (data_paramters) {
		var complemento = $scope.contact_selected.complemento;
		complemento === null? complemento='' : {} ;

		return (!($scope.contact_selected.name === data_paramters.name
				&& $scope.contact_selected.phone === data_paramters.phone
				&& $scope.contact_selected.ddd === data_paramters.ddd
				&& $scope.contact_selected.type_contact === data_paramters.type_contact
				&& data_paramters.complemento === complemento))
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
	$scope.changing_email = false
	$scope.entity_selected = null


	$('#modal_add_email').on('hidden.bs.modal', function () {
		$(this).find("input,textarea,select").val('').end();
		$scope.email_selected.selected = '';
		$scope.changing_email = false;
		$scope.email_selected = null;
		clean_wrong_field('email');
		clean_wrong_field('nome');
		clean_wrong_field('send_xml');
		clean_wrong_field('send_suitcase');
		$scope.$apply()
	});

	$scope.reset_email = function () {
		$scope.email_selected = null
		$scope.changing_email = false
		$scope.entity_selected = null
	};

	$scope.load_field_email = function () {
		alert("Vindo aqui")
		$scope.changing_email = true;
		var xml = "False";
		var suitcase = "False";
		if ($scope.email_selected.send_xml === 'Sim'){
			xml = "True";
		}
		if ($scope.email_selected.send_suitcase === 'Sim') {
			suitcase = "True";
		}
		//alert("XML:"+xml+"\nSC:"+suitcase)
		$('#email').val($scope.email_selected.email);
		$('#name').val($scope.email_selected.name);
		document.getElementById('send_xml').value=xml;
		document.getElementById('send_suitcase').value=suitcase;
	}

	$scope.change_email = function () {
		var data_paramters = {
				id : $scope.email_selected.id,
				email :$('#email').val(),
        name : $('#name').val(),
        send_xml : $('#send_xml').val(),
				send_suitcase : $('#send_suitcase').val()
		}

		success_function = function () {
			$scope.load_emails();
			$('#modal_add_email').modal('hide');
			notify('success','Email Alterado','Seu email foi alterado com sucesso')
		}

		fail_function = function () {
			notify("error","Email não alterado",'Não consiguimos alterar o email')
		}
		request_api("/api/entity/update/email", data_paramters, validate_email, success_function, fail_function)
	}

	$scope.save_email = function () {
		$scope.entity_selected = angular.element(document.getElementById('identification_controller')).scope().entity_selected
		var id_entity = $scope.entity_selected.id
		var data_paramters = {
			email : $('#email').val(),
			name : $('#name').val(),
			send_xml : $('#send_xml').val(),
			send_suitcase : $('#send_suitcase').val(),
			type_class : 'Email'
		}

		sucess_function = function () {
			$scope.load_emails()
			$('#modal_add_email').modal('hide')

		}

		fail_function = function () {
			notify('error','Falha na operação','Não foi possível savar o email')
		}
		request_api("/api/entity/register/email/" + id_entity +"/", data_paramters, validate_email, sucess_function, fail_function)

	}

	$scope.load_emails = function () {
		$scope.reset_email();
		$scope.entity_selected =  angular.element(document.getElementById('identification_controller')).scope().entity_selected;
		var id = $scope.entity_selected.id
		var type_class = 'Email'
		$.ajax({
				type: 'GET',
				url: "/api/entity/list/emails/" + id +'/' + type_class +'/',

				success: function (data) {
					$scope.emails = JSON.parse(data)
					$scope.$apply();
				},

				failure: function (data) {
					alert("Não foi possivel carregar a lista")
			}
		});
		$scope.$apply();
	};

	$scope.delete_email = function () {
		var email_delete = $scope.email_selected.id
		$.ajax({
			/*O ultimo elemento da url é o tipo*/
			url: "/api/entity/delete/phone/" + email_delete + "/Email",
			success : function () {
				$scope.email_selected = null;
				$scope.load_emails();
				notify('success','Email Removido','Seu email foi removido do sistema');
				$scope.$apply()
			}
		})

	};

	/*Functions para controlar linhas da tabela*/
	$scope.select_email = function(email){
    if ($scope.email_selected !==  null){
      if($scope.email_selected == email){
        $scope.unselect_row_email();
      }
      else{
        $scope.unselect_row_email();
        $scope.select_row_email(email);
        //$scope.carregar_indicacao_selecionada();
      }
    }
    else{
      $scope.select_row_email(email);
    }
    $scope.$apply();
  }

  $scope.select_row_email = function (email) {
  	$scope.email_selected = email;
		$scope.email_selected.selected = 'selected';
  }

  $scope.unselect_row_email = function () {
		$scope.email_selected.selected = '';
    $scope.email_selected = null;
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
