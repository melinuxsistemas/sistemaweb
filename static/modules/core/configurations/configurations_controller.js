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
      url: "/api/core/configurations/backups",

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
});