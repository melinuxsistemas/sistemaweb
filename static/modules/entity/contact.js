//Validadores do modulo de contatos

function validate_contact(){
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
	alert('vou retornar')
	return true
}

function is_a_number(string) {
	return !(isNaN(string))
}

function  validate_email() {
	alert("Olhao q eu estou pegando"+$('#email').val())
	var response = email_is_valid('email')
	alert("Olha o return"+response)
	return response
}
