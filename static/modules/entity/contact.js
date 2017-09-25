//Validadores do modulo de contatos

function validate_contact(){
  //var cpf_cnpj = $('#cpf_cnpj').val();
	var cpf_cnpj = '14960175796'
	if ( cpf_cnpj == ''){
    notify('error','Sem registro',"Primeiro cadastre nova entidade");
    return false
  }
  return true
}

function  validate_email() {
	alert("Olhao q eu estou pegando"+$('#email').val())
	var response = email_is_valid('email')
	alert("Olha o return"+response)
	return response
}
