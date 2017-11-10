function validate_permission (dict){
	for (var string_menu in dict){
		var list_permissions = dict[string_menu].replace(/;/g,'');
		if (!(menus_is_numeric_limits(list_permissions)) || (validate_size_menus(list_permissions,string_menu))){
			return error_notify(string_menu,"Campo com conteudo imprópio","Preencha os campos selecionando as estrelas")
		}


	}
	return true
}

function menus_is_numeric_limits(list_permissions) {
	for (var i=0; i<list_permissions.length;i++){
		var isnum =/^\d+$/.test(list_permissions[i])
		if((list_permissions[i]<0) || (list_permissions[i]>5) || !(isnum)) {
			return false
		}
	}
	return true
}


function validate_size_menus (list_permission,menu){
	alert("vindo")
	for (var i=0; i<list_permission.length;i++){
		alert("OLHA O TAMNHO Q EU TRAGO:"+list_permission.length)
		alert("OLHA O TAMANHO EXIGIDO:"+JSON.stringify($scope.lista_all_menus))
		if ($scope.lista_all_menus[menu][i].length != list_permission.length){
			alert("TAMANHOS DIFERENTES")
			return false
		}
	}
	return true
}