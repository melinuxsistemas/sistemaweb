function get_custom_messages(){
  var messages = {
        invalid         : 'Informe nome contendo apenas letra e sem duplo espaço!',
        short           : 'Informe nome completo!',
        long            : 'Informe no máximo x caracteres!',
        checked         : 'must be checked',
        empty           : 'Campo obrigatório!',
        select          : 'Please select an option',
        number_min      : 'too low',
        number_max      : 'too high',
        url             : 'invalid URL',
        number          : 'not a number',
        email           : 'email address is invalid',
        email_repeat    : 'emails do not match',
        date            : 'data inválida',
        time            : 'invalid time',
        password_repeat : 'Senhas não conferem!',
        no_match        : 'no match',
        complete        : 'Informe o nome completo'
      }
    return messages;
}

function validate_all_form (){
	var validator = new FormValidator();
	validator.texts = get_message_validators();
	validator.settings.alerts = true;

	result = validator.checkAll($('#form-save-entity'));
	return result.valid
}

function validate_field_entity (id_field){
	var campo = $('#'+id_field).val()
	var validator = new FormValidator();
	validator.texts = get_custom_messages();
	validator.settings.alerts = true;
	var result = validator.checkField($('#'+id_field));
  return result.valid
}











function reset_entity_form(){
	document.getElementById("form-save-entity").reset();
	select_selectpicker('natureza_juridica',null)
	select_selectpicker('relations_company',[])
	select_selectpicker('market_segments',[])
	select_selectpicker('buy_destination',[])
	select_selectpicker('company_activities',[])
}

function select_entity_type(){
	var entity_type = parseInt($("#entity_type").val())
	//alert('vou ver o tipo: '+entity_type)
	if(entity_type == 1){

		$("#lb_cpf_cnpj").text('CPF')
		$("#lb_entity_name").text('Nome Completo')
		$("#lb_fantasy_name").text('Apelido')
		$("#lb_birth_date_foundation").text('Data de Nascimento')
		$('#cpf_cnpj').mask('999.999.999-99');
		$('#cpf_cnpj').val('');


		select_selectpicker('natureza_juridica',0)
		select_selectpicker('main_activity',0)
		select_selectpicker('tributary_regime',0)
		$('#market_segments').selectpicker('deselectAll');
		$('#buy_destination').selectpicker('deselectAll');
		$('#company_activities').selectpicker('deselectAll');
		

		desable_selectpicker('natureza_juridica')
		desable_selectpicker('main_activity')
		desable_selectpicker('market_segments')
		desable_selectpicker('tributary_regime')
		desable_selectpicker('company_activities')
		desable_selectpicker('buy_destination')

		$('#field_natureza_juridica').hide();
		$('#field_main_activity').hide();
		$('#field_tributary_regime').hide();
		$('#field_company_activities').hide();
		$('#field_buy_destination').hide();
		$('#field_market_segments').hide();

		$('#field_entity_father').show();
		$('#field_entity_mother').show();
		$('#field_entity_conjuge').show();
		$('#field_entity_occupation').show();
		//$('#tributary_regime').selectpicker('val', 0);
	}

	else if(entity_type == 2){
		//alert("TROCAR PRA PESSOA JURIDICA")
		$("#lb_cpf_cnpj").text('CNPJ')
		$("#lb_entity_name").text('Razão Social')
		$("#lb_fantasy_name").text('Nome Fantasia')
		$("#lb_birth_date_foundation").text('Data de Fundação')
		$('#cpf_cnpj').mask('99.999.999/9999-99');

		$('#cpf_cnpj').val('');

		enable_selectpicer('natureza_juridica')
		enable_selectpicer('main_activity')
		enable_selectpicer('market_segments')
		enable_selectpicer('tributary_regime')
		enable_selectpicer('company_activities')
		enable_selectpicer('buy_destination')

		$('#field_natureza_juridica').show();
		$('#field_main_activity').show();
		$('#field_tributary_regime').show();
		$('#field_company_activities').show();
		$('#field_buy_destination').show();
		$('#field_market_segments').show();

		$('#field_entity_father').hide();
		$('#field_entity_mother').hide();
		$('#field_entity_conjuge').hide();
		$('#field_entity_occupation').hide();
		//$('#tributary_regime').selectpicker('val', 2);
	}

	else{
		//alert("TROCAR PRA ORGAO PUBLICO")
		$("#lb_cpf_cnpj").text('CNPJ')
		$("#lb_entity_name").text('Razão Social')
		$("#lb_fantasy_name").text('Sigla')
		$("#lb_birth_date_foundation").text('Data de Fundação')
		$('#cpf_cnpj').mask('99.999.999/9999-99');
		$('#cpf_cnpj').val('');

		enable_selectpicer('natureza_juridica')
		desable_selectpicker('main_activity')
		desable_selectpicker('tributary_regime')
		desable_selectpicker('company_activities')
		enable_selectpicer('market_segments')
		enable_selectpicer('buy_destination')

		$('#field_natureza_juridica').show();
		$('#field_main_activity').show();
		$('#field_tributary_regime').show();
		$('#field_company_activities').show();
		$('#field_buy_destination').show();
		$('#field_market_segments').show();

		$('#field_entity_father').hide();
		$('#field_entity_mother').hide();
		$('#field_entity_conjuge').hide();
		$('#field_entity_occupation').hide();
	}

	//alert("realizei a troca")
}