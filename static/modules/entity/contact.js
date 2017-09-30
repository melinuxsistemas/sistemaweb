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
	return (validate_phone_ddd())
}

function is_a_number(string) {
	return !(isNaN(string))
}


function  validate_email() {
	var response = email_is_valid('email')
	return response
}
