/**
 * Created by diego on 14/11/2017 - 14:42.
 */
var application = angular.module('modules.configurations', ['angularUtils.directives.dirPagination']);
application.controller('configurations_controller', function ($scope) {

	$scope.backups = null;
	$scope.loaded_backups = false;

	$scope.load = function () {
    $.ajax({
      type: 'GET',
      url: "/api/core/configurations/backup",

      success: function (data) {
        $scope.backups = JSON.parse(data).object;
        $("#loading_tbody").fadeOut();
        $scope.$apply();
        $scope.loaded_backups = true;
        $scope.$apply();
      },

      failure: function (data) {
        $scope.loaded_backups = true;
        alert("Não foi possivel carregar a lista")
      },
    })
	}

	$scope.create_backup = function () {
		NProgress.start();
		var start_request = Date.now();
		$.ajax({
      type: 'GET',
      url: "/api/core/configurations/backup/create",

      success: function (data) {
      	var response = JSON.parse(data);
      	var item = response.object;
      	alert(JSON.stringify(item));
      	var result = response.result
      	if(result=true){
      		$scope.backups.splice(0, 0, item);
					$scope.$apply();
      	}
      	register_action(start_request, status)
      	NProgress.done();
      },

      failure: function (data) {
      	alert("Não foi possivel carregar a lista")
        $scope.loaded_backups = true;
        register_action(start_request, status)
      	NProgress.done();
      },
    })
	}
});