// Modulo de controle de parametros da tela
function verify_screen_paramters(){
	var SCREEN_PARAMTERS = {}
	screen_width = window.innerWidth
	screen_height = window.innerHeight
	SCREEN_PARAMTERS['screen_width'] = screen_width
	SCREEN_PARAMTERS['screen_height'] = screen_height
	/*
	$scope.S9 = false;  // Giant Screen:   1921 or more
	$scope.S8 = false;  // Larger Screen:  1680 ~ 1920
	$scope.S7 = false;  // Giant Screen:   1367 ~ 1680
	$scope.S6 = false;  // Larger Screen:  1025 ~ 1366
	$scope.S5 = false;  // Giant Screen:    801 ~ 1024
	$scope.S4 = false;  // Larger Screen:   641 ~ 800
	$scope.S3 = false;  // Large Screen:    481 ~ 640
	$scope.S2 = false;  // Medium Screen:   321 ~ 480
	$scope.S1 = false;  // Small Screen:    241 ~ 320
	$scope.S0 = false;  // Smaller Screen:    0 ~ 240
	*/

	if (screen_width <= 240){ SCREEN_PARAMTERS['screen_model'] = 0; }
	else if (screen_width <= 320){ SCREEN_PARAMTERS['screen_model'] = 1; }
	else if (screen_width <= 480){ SCREEN_PARAMTERS['screen_model'] = 2;	}
	else if (screen_width <= 640){SCREEN_PARAMTERS['screen_model'] = 3; }
	else if (screen_width <= 800){ SCREEN_PARAMTERS['screen_model'] = 4; }
	else if (screen_width <= 1024){ SCREEN_PARAMTERS['screen_model'] = 5; }
	else if (screen_width <= 1366){ SCREEN_PARAMTERS['screen_model'] = 6; }
	else if (screen_width <= 1680){ SCREEN_PARAMTERS['screen_model'] = 7; }
	else if (screen_width <= 1920){ SCREEN_PARAMTERS['screen_model'] = 8; }
	else{ SCREEN_PARAMTERS['screen_model'] = 9; }

	pagination_itens_per_page = parseInt((screen_height/26)-12);
	table_minimal_rows = Array.apply(null, Array(pagination_itens_per_page)).map(function (x, i) { return i; });
	total_rows_height = pagination_itens_per_page*28;

	if (pagination_itens_per_page < 2){
		pagination_itens_per_page = 2;
	}

	SCREEN_PARAMTERS['table_maximun_items_per_page'] = pagination_itens_per_page
	SCREEN_PARAMTERS['table_maximun_body_height'] = total_rows_height
	SCREEN_PARAMTERS['table_minimun_items'] = table_minimal_rows

	return SCREEN_PARAMTERS
}

SCREEN_PARAMTERS = verify_screen_paramters();

window.onresize = function(event) {
	SCREEN_PARAMTERS = verify_screen_paramters();
	post_screen_verified()
};

