//Validadores do modulo de contatos

function validate_contact(){
  //var cpf_cnpj = $('#cpf_cnpj').val();
	var cpf_cnpj = '14960175796'
	if ( cpf_cnpj == ''){
    alert("Sem cpf");
    return false
  }
  return true
}