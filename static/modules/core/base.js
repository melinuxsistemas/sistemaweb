/**
 * Created by diego on 03/05/2017.
 */
function notify(type,title,description){
  new PNotify({
    title: title,
    text: description,
    //auto_display: false,
    hide: true,
    delay: type=='error' ? 5000 : 2000,
    mouse_reset: false,
    type: type,
    styling: 'bootstrap3' // bootstrap3 , fontawesome
  });
  return (type=='error' ? false : true);
}

function info_notify(title,description){
  return notify("info",title,description);
}

function success_notify(title,description){
  return notify("success",title,description);
}

function error_notify(id,title,description){
  document.getElementById(id).focus();
  return notify("error",title,description);
}

function warning_notify(id,titulo,descricao){
  document.getElementById(id).focus();
  return notify("warning",titulo,descricao);
}

function contains_minimal_size(id,size){
  return (document.getElementById(id).value.length>=size);
}

function contains_numeric(id){
  var numbers = /\d+/g;
  return (document.getElementById(id).value.match(numbers) ? true : false);
}

function contains_alpha(id) {
  var letters = /[a-zA-Z]+/;
  return (document.getElementById(id).value.match(letters) ? true : false);
}

function is_empty(id){
  return (document.getElementById(id).value.length == 0 ? !error_notify(id,"Campo Obrigatório","Por favor preencha o campo.") : false)
}

function email_is_valid(id) {
  var filter = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
  if(!is_empty(id)){
    if(filter.test(document.getElementById(id).value)){
      return true;
    }
    else{
      return error_notify("email","Email Inválido","Verifique se o email foi digitado corretamente.")
    }
  }
  else{
    return false;
  }
}
