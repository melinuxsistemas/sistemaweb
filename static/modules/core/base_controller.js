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
	var start_request = Date.now();
  $.ajax({
    type: request_method,
    url: url,
    data: data_paramters,
    success: function(data) {
			var response = $.parseJSON(data);
      var message = response['message']
      var result = response['result']
      var data_object = response['object'];//$.parseJSON()
      var status = response['status']

      if (result == true) {
        //var moment_date = moment(data_object['fields']['joined_date']).format("DD/MM/YYYY - HH:mm:ss")
        if (success_function != null) {
        	var redirect = success_function(result,message,data_object,status);
        }
      }

      else {
        if( typeof message === 'string' ) {
          notify('error',"Falha na operação",message)
        }
        else {
        	if(fail_function != null){
        		fail_function(result,message,data_object,status);
        	}
        }
      }

     	register_action(start_request, status)
      NProgress.done();
      if (redirect){
      	window.location = redirect;
      }
      return true;
    },
    failure: function(data){
    	NProgress.done();
      register_action(start_request,status.request_path, status.request_size, status.server_processing_time_duration, status.cliente_processing_time_duration)
    }
  });
}