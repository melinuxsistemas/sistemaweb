function clear_mask_numbers(value){
  var number = value.split('.').join('');
  number = number.split('-').join('');
  return number;
}


function validate_general_form(){
  var messages = {
        invalid         : 'Informe numeros e letras!',
        short           : 'Informe pelo menos 8 caracteres!',
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
        date            : 'invalid date',
        time            : 'invalid time',
        password_repeat : 'Senhas não conferem!',
        no_match        : 'no match',
        complete        : 'Informe o nome completo'
      }

      var validator = new FormValidator();
      validator.texts = messages;
      validator.settings.alerts = true;

      result = validator.checkAll($('#form-save-entity'))
      return result.valid
  //return true;//(email_is_valid("email") && validate_password("senha"));
}

function validate_form_regiter_entity (){
    return (validate_cpf("cpf_cnpj") && validate_date("birth_date_foundation" && validate_general_form()))
}

/*
function validate_form_confirm_register(){
  return (email_is_valid("email"));
}

function validate_form_reset_password(){
  return (email_is_valid("email"));
}

function validate_form_change_password(){
  var messages = {
        invalid         : 'Informe numeros e letras!',
        short           : 'Informe pelo menos 8 caracteres!',
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
        date            : 'invalid date',
        time            : 'invalid time',
        password_repeat : 'Senhas não conferem!',
        no_match        : 'no match',
        complete        : 'input is not complete'
      }

      var validator = new FormValidator();
      validator.texts = messages;
      validator.settings.alerts = true;

      result = validator.checkAll($('#form_change_password'))
      return result.valid
  //return true;//(email_is_valid("email") && validate_password("senha"));
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

*/
function validate_date(birth_date_foundation) {
    var data = $('#'+birth_date_foundation).val();
    var date_current = new Date;
    var year_current = date_current.getFullYear();
    var split = data.split('/');
    var year_data = split[2];
    var age = year_current - year_data;
    if(age < 18 && age>0){
        return error_notify("birth_date_foundation","Data de nascimento inválida","Não pode cadastrar pessoas com menos de 18 anos");
    }
    if (age>150){

        return error_notify("birth_date_foundation","Data informada não é valida","Não se pode cadastrar pessoas com idade acima de 150 anos")
    }
    if (age < 0){
        return error_notify("birth_date_foundation","Data informada não é válida","Não se pode cadastrar datas futuras")
    }
    return true;
}

function validate_entity_name (entity_name){
    var name = $('#'+ entity_name).val();
    if (name === ''){
        error_notify ('entity_name','Nome de entidade inválido','Informe um nome')
    }
    var entity_slplit = name.split(' ');
    if (entity_slplit[0] === '' || entity_slplit[1] === ''){
        return error_notify ('entity_name','Nome de entidade inválido','Espaços excedendes')
    }
    if (entity_slplit.length < 2 ){
        return error_notify ('entity_name','Nome de entidade inválido','Nome informado é muito curto')
    }
    return true
}

function validate_cpf (cpf_cnpj){
    var cpf = $('#'+cpf_cnpj).val();
    cpf = cpf.replace(/[^\d]+/g,'');
    if(cpf === "") {
        return error_notify("cpf_cnpj","Campo obrigatório","Insira um cpf");
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
        return error_notify("cpf_cnpj","CPF inválido","Cadastre um cpf válido");
    }
    // Valida 1o digito
    var add = 0;
    for (i=0; i < 9; i ++)
        add += parseInt(cpf.charAt(i)) * (10 - i);
        var rev = 11 - (add % 11);
        if (rev === 10 || rev === 11)
            rev = 0;
        if (rev !== parseInt(cpf.charAt(9)))
            return error_notify("cpf_cnpj","CPF inválido","Cadastre um cpf válido");
    // Valida 2o digito
    add = 0;
    for (i = 0; i < 10; i ++)
        add += parseInt(cpf.charAt(i)) * (11 - i);
    rev = 11 - (add % 11);
    if (rev === 10 || rev === 11) {
        rev = 0;
    }
    if (rev !== parseInt(cpf.charAt(10))){
        return error_notify("cpf_cnpj","CPF inválido","Cadastre um cpf válido");
    }
    return true;
}