application.controller('register_phone_entity', function ($scope) {
	$scope.contacts = [];
	$scope.contact_selected = null;
	$scope.changing_contact = false;
	$scope.entity_selected = null;
	$scope.minimal_rows_tables = [0,1,2,3,4,5,6,7,8,9];
	$scope.maskuse = null;
	$scope.maskuse_ddd = null;


	$('#type_contact').change(function() {

		var type = $('#type_contact').val();
		var maskuse;
		$("#phone_number").val('');
		$("#ddd").val('');

		if (type == 1 ) {
			$scope.maskuse =  "99999-9999";
			$scope.maskuse_ddd = "(99)";
		}
		if (type ==2 || type==4) {
			$scope.maskuse =  "9999-9999";
			$scope.maskuse_ddd = "(99)";
		}
		if (type == 3) {
			$scope.maskuse =  "999-9999";
			$scope.maskuse_ddd = "9999";
		}
		$("#phone_number").mask($scope.maskuse);
		$("#ddd").mask($scope.maskuse_ddd);
		$scope.maskuse = null;
		$scope.maskuse_ddd = null

});





	/*Quando o modal ficar off, limpamos os campos e as variaveis controladoras, remover class wrong_field*/
	$('#modal_add_phone').on('hidden.bs.modal', function () {
		$(this).find("input,textarea,select").val('').end();
		$scope.contact_selected.selected = '';
		$scope.changing_contact = false;
		$scope.contact_selected = null;
		$('#type_contact').val(1);
		clean_wrong_field('ddd');
		clean_wrong_field('phone');
		$scope.$apply()
	});

	/*RESETAR DADOS PARA TRATAR A TROCA DE CONTATOS SEM ABRIR MODAL*/
	$scope.reset_contact = function () {
		$scope.contacts = [];
		$scope.contact_selected = null;
		$scope.changing_contact = false;
		$scope.entity_selected = null
	};
	/*Controller of contacts*/
	$scope.save_tel = function () {
		$scope.contact_selected = null;
		var id_entity = angular.element(document.getElementById('identification_controller')).scope().entity_selected.id;
		var data_paramters = {
			type_contact: $('#type_contact').val(),
			name: $('#name_contact').val().toUpperCase(),
			ddd: clear_mask_numbers_contact($('#ddd').val()),
			phone: clear_mask_numbers_contact($('#phone_number').val()),
			complemento: $('#complemento').val().toUpperCase(),
			id_entity: id_entity
		};

		success_function = function (result,message,data_object) {
			notify('success','Contato Adicionado','Seu contato foi registrado');
			var new_contact = data_object;
			alert(new_contact.type_contact);
			$scope.contacts.push(new_contact);
			$scope.$apply();
			$('#modal_add_phone').modal('hide')

		}

		fail_function = function (message) {
			notify('error','Error ao tentar salvar','Não foi possivel salvar o contato')
		}
		request_api("/api/entity/register/contact/", data_paramters, validate_contact, success_function, fail_function)
	};

	/*Carregar Lista com os contatos*/
	$scope.load_contacts = function () {
		$scope.entity_selected =  angular.element(document.getElementById('identification_controller')).scope().entity_selected;
		var id = $scope.entity_selected.id;
		$('#title_contact').text($scope.entity_selected.entity_name)

		var data_paramters = {
			id : id
		};

		success_function = function (result,message,data_object,status) {
				$scope.contacts = data_object;
				$scope.$apply();
		};

		fail_function = function () {
			notify('error','Falha ao Carregar','Não foi possivel carregar os contatos.')
		};

		validate_function = function () {
			return true;
		};

		request_api("/api/entity/contacts/",data_paramters,validate_function,success_function,fail_function)
		$scope.$apply();
	};

	/*Deletar contato*/
	$scope.delete_contact = function () {
		var id_contact = $scope.contact_selected.id;
		$.ajax({
			url: "/api/entity/delete/phone/" + id_contact ,

			success : function () {
				var pos = $scope.contacts.indexOf($scope.contact_selected)
				$scope.contacts.splice(pos,1);
				$scope.contact_selected = null
				notify('success','Contato Removido','Seu contato foi removido do sistema')
				$scope.$apply()
			},
		})
	};

	/*Função que carreaga os campos do formulario de Contatos*/
	$scope.load_field_contact = function () {
		$scope.changing_contact = true;
		//$('#type_contact :selected').text(($scope.contact_selected.type_contact));
		$('#type_contact').val($scope.contact_selected.id_type_contact);
		$('#phone_number').val($scope.contact_selected.phone);
		$('#ddd').val($scope.contact_selected.ddd);
		$('#name_contact').val($scope.contact_selected.name)
		$('#complemento').val($scope.contact_selected.complemento)
	};

	/*Função para atualizar cotato*/
	$scope.change_contact = function () {
		var data_paramters = {
			id : $scope.contact_selected.id,
			type_contact: $scope.contact_selected.type_contact,
			name: $('#name_contact').val().toUpperCase(),
			ddd: clear_mask_numbers_contact($('#ddd').val()),
			phone: clear_mask_numbers_contact($('#phone_number').val()),
			complemento: $('#complemento').val().toUpperCase()
		};

		/*Verifica se o modal Alterar possui mudanças*/
		if ($scope.equals_fields_contact(data_paramters)) {
				success_function = function (result,message,data_object) {
					var contact = data_object;
					var index = $scope.contacts.indexOf($scope.contact_selected)
					$scope.contacts.splice(index,1);
					$scope.contacts.splice(index,0, contact);
					$('#modal_add_phone').modal('hide');
					notify('success','Contato Alterado',"Seu contato foi atualizado com sucesso")
					$scope.$apply();
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
	};

	/*Função que verifica se existe mudança no formulário*/
	$scope.equals_fields_contact = function (data_paramters) {
		var complemento = $scope.contact_selected.complemento;
		complemento === null? complemento='' : {} ;

		return (!($scope.contact_selected.name === data_paramters.name
				&& $scope.contact_selected.phone === data_paramters.phone
				&& $scope.contact_selected.ddd === data_paramters.ddd
				&& $scope.contact_selected.type_contact === data_paramters.type_contact
				&& data_paramters.complemento === complemento))
	};

	/*Funções para controlar seleção de linha da tabela de contatos*/
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
  };

  $scope.select_row_contact = function (contact) {
  	$scope.contact_selected = contact;
		$scope.contact_selected.selected = 'selected';
  };

  $scope.unselect_row_contact = function () {
		$scope.contact_selected.selected = '';
    $scope.contact_selected = null;
  };



	/*$scope.check_disable = function () {
		if ($scope.email_selected == null){
			return true
		}else{
			return false
		}
	};*/


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
	$scope.emails = [];
	$scope.email_selected = null;
	$scope.changing_email = false;
	$scope.entity_selected = null;
	$scope.minimal_rows_table_email = [0,1,2,3,4,5,6,7,8,9]//angular.element(document.getElementById('contact_controller')).scope().minimal_rows_tables;



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
		$scope.email_selected = null;
		$scope.changing_email = false;
		$scope.entity_selected = null;
	};

	$scope.load_field_email = function () {
		$scope.changing_email = true;
		var xml = "False";
		var suitcase = "False";
		if ($scope.email_selected.send_xml === true || $scope.email_selected.send_xml === 'True'){
			xml = "True";
		}
		if ($scope.email_selected.send_suitcase === true ||  $scope.email_selected.send_suitcase === 'True') {
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
        name : $('#name').val().toUpperCase(),
        send_xml : $('#send_xml').val(),
				send_suitcase : $('#send_suitcase').val()
		}

		success_function = function (result,message,data_object) {
			var data_email = data_object;
			var index = $scope.emails.indexOf($scope.email_selected)
			$scope.emails.splice(index,1);
			$scope.emails.splice(index,0,data_email);
			alert(JSON.stringify(data_email))
			$('#modal_add_email').modal('hide');
			$scope.$apply();
			notify('success','Email Alterado',"Seu email foi atualizado com sucesso")
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
			name : $('#name').val().toUpperCase(),
			send_xml : $('#send_xml').val(),
			send_suitcase : $('#send_suitcase').val(),
			id_entity : id_entity
		};

		sucess_function = function (result,message,data_object) {
			var data_email = data_object;
			$scope.emails.push(data_email);
			notify('success','Email salvo','Seu Email foi salvo com sucesso');
			$('#modal_add_email').modal('hide');
			$scope.$apply()

		};

		fail_function = function () {
			notify('error','Falha na operação','Não foi possível savar o email')
		};
		request_api("/api/entity/register/email", data_paramters,validate_email, sucess_function, fail_function)

	}

	$scope.load_emails = function () {
		$scope.reset_email();
		$scope.entity_selected =  angular.element(document.getElementById('identification_controller')).scope().entity_selected;
		var id = $scope.entity_selected.id;
		$.ajax({
				type: 'GET',
				url: "/api/entity/list/emails/" + id +'/',

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
		var email_delete = $scope.email_selected.id;
		$.ajax({
			/*O ultimo elemento da url é o tipo*/
			url: "/api/entity/delete/email/" + email_delete,
			success : function () {
				var pos = $scope.emails.indexOf($scope.email_selected)
				$scope.emails.splice(pos,1);
				$scope.email_selected = null;
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

  /*$scope.update_minimal_table = function () {
		var emails = $scope.emails.length
		alert(emails)
		var lenght = $scope.minimal_rows_table_email.length
		alert(lenght)
		if (lenght <=  emails){
			$scope.minimal_rows_table_email.push(1)
			alert("Olha o lista"+$scope.minimal_rows_table_email);
			angular.element(document.getElementById('contact_controller')).scope().minimal_rows_tables = $scope.minimal_rows_table_email
			$scope.$apply();
			alert("Olha A lista agora	"+angular.element(document.getElementById('contact_controller')).scope().minimal_rows_tables)
		}
	}*/




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
