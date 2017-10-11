//Validadores do modulo de contatos
function validate_phone_ddd() {
	clean_wrong_field('ddd');
	clean_wrong_field('phone');
	var error = false;
	var ddd = $('#ddd').val();
	var phone =$('#phone_number').val();
	if (!is_a_number(phone)){
		set_wrong_field('phone','Campo contém letras');
		error = true
	}
	if (!is_a_number(ddd)){
		set_wrong_field('ddd','Campo contém letras')
		error = true
	}
	if (error) {
		notify('error','Numero ou DDD inválido','Esses campos só podem conter numeros')
		return false
	}
	return true
}

function validate_contact(){
	/*Criar validações para campos vazios*/
	return (validate_phone_ddd() && not_empty('name_contact') && not_empty('phone_number') && not_empty('ddd'))
}

function not_empty(field) {
	if ($('#'+field).val() != ''){
		return true
	}
	return false
}
function is_a_number(string) {
	return !(isNaN(string))
}

function field_empty(field) {
	var test_field = $('#'+field).val();
	if (test_field === null || test_field === ''){
		set_wrong_field(field,'informe esse campo')
		return false
	}
	return true
}

function  validate_email() {
	var response = email_is_valid('email');
	var empty_xml = field_empty('send_xml');
	var empty_suitcase = field_empty('name');
	var empty_name = field_empty('send_suitcase');
	return response && empty_xml && empty_suitcase && empty_name;
}
