/**
 * Created by diego on 03/05/2017.
 */
function notify(type,title,description){
  new PNotify({
    title: title,
    text: description,
    width: type=='confirm' ? '400px' : "300px",
    hide: type=='confirm' ? false : true,
    delay: type=='error' ? 5000 : 4000,
    mouse_reset: false,
    type: type=='confirm' ? 'success' : type,
    styling: 'bootstrap3' // bootstrap3 , fontawesome
  }
  );
  return (type=='error' ? false : true);
}

function confirm_notify(title,description){
  return notify("confirm",title,description);
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


$('.selectpicker').on('changed.bs.select', function (event ,clickedIndex, newValue, oldValue) {
	$(this).selectpicker('refresh');
});

function select_selectpicer(field_id,val){
	$('#'+field_id).selectpicker('val', val);
  $('#'+field_id).selectpicker('refresh');
}

function desable_selectpicer(select_id){
	$('#'+select_id).prop('disabled', true);
	$('#lb_'+select_id).addClass('disabled');
  $('#'+select_id).selectpicker('refresh');
}

function enable_selectpicer(select_id){
	$('#'+select_id).prop('disabled', false);
	$('#lb_'+select_id).removeClass('disabled');
  $('#'+select_id).selectpicker('refresh');
}

$(".menu-header").click(function(){
  desable_new_label(this);
});

$(".child_menu .current_page").ready(function(){
  desable_new_label(this);
})

function desable_new_label(campo){
  $(campo).find('.label_new').each(function(index,object) {
    if (object.className.indexOf("label_fade") == -1){
      setTimeout(function(){ object = object.className+=' label_fade'; }, 3000);
    }
  })
}





function select_rating(select_name, value) {
  //document.querySelector('input[name="ratingtwo"]:checked').value
  //alert("consigo ver o valor:"+$('#Entidade').val())
  $("#fieldset_"+select_name+" input[type=radio]").each(function (){

    if( this.value <= value){
      $("#rate_label_"+select_name+"_"+this.value).addClass('selected_rating')
    }else{
      $("#rate_label_"+select_name+"_"+this.value).addClass('unselected_rating')
    }
  })
}
