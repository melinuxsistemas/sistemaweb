function validate_permission (dict){
	for (var string_menu in dict){
		var list_permissions = dict[string_menu].replace(/;/g,'');
		if (!(menus_is_numeric_limits(list_permissions))){
			return error_notify(string_menu,"Campo com conteudo imprópio","Preencha os campos selecionando as estrelas")
		}


	}
	return true
}

function menus_is_numeric_limits(list_permissions) {
	/*for (var i = 0; i < list_permissions.length; i++) {
		var isnum = /^\d+$/.test(list_permissions[i])
		if ((list_permissions[i] < 0) || (list_permissions[i] > 5) || !(isnum)) {
			return false
		}
	}*/
	return true
}