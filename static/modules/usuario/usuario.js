function validate_form_change_password(){
  return true;//(email_is_valid("email") && validate_password("senha"));
}

function validate_form_login(){
  return (email_is_valid("email") && validate_password("password"));
}

function validate_form_register(){
  return (email_is_valid("email") && validate_password("password")) && compare_passwords("password","confirm_password");
}

function validate_password(senha){
  if (!is_empty(senha) && check_password_format(senha)){
    return true;
  }
  else{
    return error_notify("password","Senhas Insegura","Informe uma senha com ao menos 8 caracteres contendo letras e numeros.");
  }
}

function check_password_format(senha){
  return ((contains_alpha(senha) && contains_numeric(senha) && contains_minimal_size(senha,8)) ? true : false);
}

function compare_passwords(id_senha, id_confirma_senha){
  var senha = document.getElementById(id_senha).value;
  var confirma_senha = document.getElementById(id_confirma_senha).value;
  return (senha === confirma_senha ? true : error_notify("confirm_password","Senhas não conferem","Verifique as senhas informadas."));
}

$('#envia').on('click',function() {
	var vazios = $("input[type=email]").filter(function() {
    return !this.value;
  }).get();

  if(vazios.length){
    error_notify('email',"Falha na operação","Informe um email válido para gerar senha.")
    return false;
  }
});
