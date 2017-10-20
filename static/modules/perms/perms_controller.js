/**
 * Created by lucas on 20/10/2017.
 */
var application = angular.module('modules.perms',[]);
application.controller('perms_controller', function($scope) {
	$scope.select_perm =function () {
		var tesste = document.querySelector('input[name="ratingtwo"]:checked').value;
		alert(tesste)
	}
});