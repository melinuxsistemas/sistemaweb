//function validate_form_regiter_person (){
//  var result = (validate_date_person("birth_date_foundation") & !is_empty('entity_name') & validate_cpf('cpf_cnpj'))
//  return result;
//}

function validate_form_entity() {
	var entity_type = $('#entity_type').val()
	if (entity_type == 1){
		alert("Eh uma pessoa fisica")
	}
	else{
		alert("eh uma pessoa juridica")
	}
	return (validate_cpf_cnpj('cpf_cnpj') && validate_date_foundation('birth_date_foundation') && validate_all_form() )
}


function validate_cpf_cnpj(){
	var value = $('#cpf_cnpj').val();
	if(value.length==14){
		validate_cpf(value);
	}
	else{
		validate_cnpj(value)
	}
}

function validate_cpf(value){
  var cpf = value;
  cpf = cpf.replace(/[^\d]+/g,'');
  var result = true;

  if (cpf == ''){
      set_wrong_field('cpf_cnpj','Campo obrigatório');
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
      set_wrong_field('cpf_cnpj', "Documento inválido.")
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
      set_wrong_field('cpf_cnpj', "Documento inválido.")
      return false; //notify("error","CPF inválido","Cadastre um cpf válido");
  }
  clean_wrong_field('cpf_cnpj')
  return true;
}

function validate_cnpj(value) {
    var cnpj = value;
    cnpj = cnpj.replace(/[^\d]+/g,'');
    var result = true;
    if(cnpj === ''){
        set_wrong_field('cpf_cnpj','Campo obrigatório.')
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
      set_wrong_field('cpf_cnpj', "Documento inválido.")
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
        set_wrong_field('cpf_cnpj','Documento inválido.')
        return false;//notify('error','CNPJ não existente','informe cnpj válido');
    }
    clean_wrong_field('cpf_cnpj')
    return true;
}

function calculate_age(data){
	var year_current = new Date().getFullYear();
	var year_date = data.split('/')[2];
	return year_current - year_date;
}

function validate_date(data){
	if(!(data === "__/__/____") && !(data === '')) {
		return true;
	}
	else{
		return false;
	}
}

function validate_birth_date_foundation() {
	var entity_type = $("#entity_type").val()
  var data = $('#birth_date_foundation').val();
  if (validate_date(data)){
  	var age = calculate_age(data);
  	if(age < 0){
  		set_wrong_field('birth_date_foundation','Informe uma data válida')
			return notify("error","Data Inválida","Data não pode ser futura.");
  	}

  	if(entity_type=='1'){
  		if (age>=18 && age<=150){
				clean_wrong_field('birth_date_foundation')
				return true;
  		}
  		else{
  			set_wrong_field('birth_date_foundation','Informe uma data válida')
				return notify("error","Data Inválida","Pessoa física precisa ter entre 18 e 150 anos.");
  		}
  	}
	}
	return true;
}

function clear_mask_numbers(value){
	value = value.replace("/","")
  var number = value.split('.').join('');
  number = number.split('-').join('');
  return number;
}