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
    	alert("VEJA O QUE VEIO: "+JSON.stringify(data))
    	var response = $.parseJSON(data);
      var message = response['message']
      var result = response['result']
      var data_object = $.parseJSON(response['object'])
      var status = response['status']

      if (result == true) {
        //var moment_date = moment(data_object['fields']['joined_date']).format("DD/MM/YYYY - HH:mm:ss")
        if (success_function != null) {
        	alert("deu certo..")
          success_function(result,message,data_object,status);
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

      var terminate_request = Date.now();
      var duration_request = terminate_request - start_request
      duration_request = duration_request/1000 // Math.floor(duration_request / (1000*60));
      alert("VEJA O STATUS: "+JSON.stringify(status))
      alert("REQUEST DURATION: "+duration_request+" - SERVER PROCESSING DURATION: "+status.server_processing_time_duration)
      NProgress.done();
      return true;
    },
    failure: function(data){
      NProgress.done();
      var terminate_request = Date.now();
      var duration_request = terminate_request - start_request
      duration_request = Math.floor(duration_request / 1000 % 60);
      alert("VEJA O STATUS: "+JSON.stringify(status))
      alert("REQUEST DURATION: "+duration_request+" seconds - SERVER PROCESSING DURATION: "+status.server_processing_time_duration+" seconds")
      //return notify('error','Falha na Operação',"Erro na requisição assincrona ao servidor.")
    }
  });
}
