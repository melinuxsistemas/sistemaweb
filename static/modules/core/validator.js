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

function  validate_field (field_id) {
    var message = get_message_validators();
    var validator = new FormValidator();
    validator.settings.alerts = true;
    validator.texts = message;
    return validator.checkField($(this))
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

function check_response_message_form(form_id, response_message){
  $(form_id +" input[type=text]").each(function () {
    var id = $(this).attr("id");
    var erro = response_message[id];
    if (erro){
      set_wrong_field(id, erro);
    }
    else{
      clean_wrong_field(id);
    }
  });
}

function set_wrong_field(id, erro_value){
  $("#field_"+id).addClass('bad')
  var myDivs = $("#field_"+id).children('div.alert');
	if(myDivs.length === 0){
			myDivs = $('<div class="alert"></div>')
					.appendTo("#field_"+id);
					//.css('opacity', 0);
	}
	$("#field_"+id+" .alert").html(erro_value);
}

function clean_wrong_field(id){
  $("#field_"+id).removeClass('bad')
  $("#field_"+id+" .alert").html("");
}