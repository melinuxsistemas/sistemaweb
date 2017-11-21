function clear_mask_numbers(value){
	value = value.replace("/","")
  var number = value.split('.').join('');
  number = number.split('-').join('');
  return number;
}

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

function validate_form_regiter_person (){
  var result = ( validate_date_person("birth_date_foundation") & !is_empty('entity_name') & validate_cpf('cpf_cnpj'))
  return result;
}

function validate_cpf (cpf_cnpj){
  var cpf = $('#'+cpf_cnpj).val();
  cpf = cpf.replace(/[^\d]+/g,'');
  var result = true;

  if (cpf == ''){
      set_wrong_field(cpf_cnpj,'Campo obrigatório');
      return false
  }
  // Elimina CPFs invalidos conhecidos
  if (cpf.length !== 11 ||
      cpf === "00000000000" ||
      cpf === "11111111111" ||
      cpf === "22222222222" ||
      cpf === "33333333333" ||
      cpf === "44444444444" ||
      cpf === "55555555555" ||
      cpf === "66666666666" ||
      cpf === "77777777777" ||
      cpf === "88888888888" ||
      cpf === "99999999999") {
      result = false;
  }
  // Valida 1o digito
  var add = 0;
  for (i=0; i < 9; i ++)
      add += parseInt(cpf.charAt(i)) * (10 - i);
      var rev = 11 - (add % 11);
      if (rev === 10 || rev === 11)
          rev = 0;
      if (rev !== parseInt(cpf.charAt(9)))
          result = false;
  // Valida 2o digito
  add = 0;
  for (i = 0; i < 10; i ++)
      add += parseInt(cpf.charAt(i)) * (11 - i);
  rev = 11 - (add % 11);
  if (rev === 10 || rev === 11) {
      rev = 0;
  }
  if (rev !== parseInt(cpf.charAt(10))){
      result = false;
  }

  if (result === false){
      set_wrong_field(cpf_cnpj, "Conteúdo inválido")
      return false; //notify("error","CPF inválido","Cadastre um cpf válido");
  }
  clean_wrong_field(cpf_cnpj)
  return true;
}

function validate_date_person(birth_date_foundation) {
  var data = $('#'+birth_date_foundation).val();

  if(!(data === "__/__/____") && !(data === '')) {
  	var date_current = new Date;
		var year_current = date_current.getFullYear();
		var split = data.split('/');
		var year_data = split[2];
		var age = year_current - year_data;
    if (age < 0){
			set_wrong_field(birth_date_foundation,'Informe uma data válida')
      return notify("error","Data Inválida","Este campo não permite data futura.")
		}

		else if(age<18 ){
			set_wrong_field(birth_date_foundation,'Informe uma data válida')
			return notify("error","Data Inválida","Pessoa física precisa ter 18 anos ou mais.");
		}
		else if (age>=18 && age<=150){
			clean_wrong_field(birth_date_foundation)
  		return true;
		}

		else{
			set_wrong_field(birth_date_foundation,'Informe uma data válida')
			return notify("error","Data Inválida","Pessoa Física precisa ter menos de 150 anos.")
		}
	}
	//Retorna True para datas vazia (Campo n obrigatório)
	return true;
}

function validate_form_regiter_company() {
    return ( validate_cnpj('cpf_cnpj') && validate_date_foundation('birth_date_foundation') && validate_all_form() )
}

function validate_cnpj(cpf_cnpj) {
    var cnpj = $('#'+cpf_cnpj).val();
    cnpj = cnpj.replace(/[^\d]+/g,'');
    var result = true;
    if(cnpj === ''){
        set_wrong_field(cpf_cnpj,'Campo obrigatório')
        return false
    }

    if (cnpj === "00000000000000" ||
        cnpj === "11111111111111" ||
        cnpj === "22222222222222" ||
        cnpj === "33333333333333" ||
        cnpj === "44444444444444" ||
        cnpj === "55555555555555" ||
        cnpj === "66666666666666" ||
        cnpj === "77777777777777" ||
        cnpj === "88888888888888" ||
        cnpj === "99999999999999")
    {
      result = false // error_notify('cpf_cnpj','CNPJ inválido','Digite um CNPJ existente')
    }

    var tamanho = cnpj.length - 2;
    var numeros = cnpj.substring(0,tamanho);
    var digitos = cnpj.substring(tamanho);
    var soma = 0;
    var pos = tamanho - 7;
    for (i = tamanho; i >= 1; i--) {
      soma += numeros.charAt(tamanho - i) * pos--;
      if (pos < 2)
            pos = 9;
    }
    var resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
    if (resultado != digitos.charAt(0)){
        result = false // error_notify('cpf_cnpj','CNPJ inválido','Digite um CNPJ ')
    }

    tamanho = tamanho + 1;
    numeros = cnpj.substring(0,tamanho);
    soma = 0;
    pos = tamanho - 7;
    for (i = tamanho; i >= 1; i--) {
      soma += numeros.charAt(tamanho - i) * pos--;
      if (pos < 2)
            pos = 9;
    }
    resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
    if (resultado != digitos.charAt(1)) {
        result = false // error_notify('cpf_cnpj', 'CNPJ inválido', 'Digite um CNPJ 22')
    }

    if (result == false ){
        set_wrong_field(cpf_cnpj,'Informe um CNPJ válido')
        return false;//notify('error','CNPJ não existente','informe cnpj válido');
    }
    clean_wrong_field(cpf_cnpj)
    return true;
}

function validate_date_foundation (birth_date_foundation){
    var data = $('#'+birth_date_foundation).val();
    var date_current = new Date;
    var year_current = date_current.getFullYear();
    var split = data.split('/');
    var year_data = split[2];
    var age = year_current - year_data;
    if(data === "__/__/____") {
        set_wrong_field(birth_date_foundation,'Campo obrigatório');

        return false
    }
    if (age < 0){
        set_wrong_field(birth_date_foundation,'Informe uma data válida')
        return notify('error',"Data informada não é válida","Não se pode cadastrar datas futuras")
    }
    clean_wrong_field(birth_date_foundation);
    return true;
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
		//alert("TROCAR PRA PESSOA FISICA")
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

		desable_selectpicer('natureza_juridica')
		desable_selectpicer('main_activity')
		desable_selectpicer('market_segments')
		desable_selectpicer('tributary_regime')
		desable_selectpicer('company_activities')
		desable_selectpicer('buy_destination')

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
		desable_selectpicer('main_activity')
		desable_selectpicer('tributary_regime')
		desable_selectpicer('company_activities')
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