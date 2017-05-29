function get_message_validators(){
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
}

function validate_form(form_id){
  var messages = get_message_validators();
  var validator = new FormValidator();
  validator.settings.alerts = true;
  validator.texts = messages;
  return validator.checkAll($(this))


  //var submit = true;


  //if(!validator.checkAll($(this))) {
    //submit = false;
    //this.submit();
  //}

  //if(submit){

  //}
  //else{
  //  return false;
  //}
}
