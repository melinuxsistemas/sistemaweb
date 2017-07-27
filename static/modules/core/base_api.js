function request_api(url,data_paramters,validator_functions,success_function,fail_function){
  var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
  data_paramters['csrfmiddlewaretoken'] = csrftoken;
  NProgress.start();
  if (validator_functions()){
    execute_ajax(url,'post',data_paramters,success_function,fail_function);
  }
  else{
      NProgress.done();
      return false;
  }
}

function execute_ajax(url,request_method,data_paramters,success_function,fail_function){
  $.ajax({
    type: request_method,
    url: url,
    data: data_paramters,
    success: function(data) {

      var response = $.parseJSON(data);
      var message = response['message']
      var resultado = response['success']
      if (resultado == true) {
        var data_object = $.parseJSON(response['data-object'])
        //var moment_date = moment(data_object['fields']['joined_date']).format("DD/MM/YYYY - HH:mm:ss")
        if (success_function != null) {
          success_function(message);
        }
      }

      else {
        if( typeof message === 'string' ) {
          notify('error',"Falha na operação",message)
        }
        else {
          fail_function(message);
        }
      }
      NProgress.done();
      return true;
    },
    failure: function(data){
      NProgress.done();
      return notify('error','Falha na Operação',"Erro na requisição assincrona ao servidor.")
    }
  });
}
