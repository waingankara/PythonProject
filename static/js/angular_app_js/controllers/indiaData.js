angular.module('covid', []).controller('covidIndia', [
    '$scope',
    '$http',
    function($scope, $http) {

    $scope.countries = ["India","Pakistan","Nepal","Sri Lanka","China"];

    $http.post('/getData', {"operation" : "firstPhase"}).then(function successCallback(response) {
		var result = JSON.parse(response.data["raw_data"]);
	    console.log(result)
	}, function errorCallback(response) {
		console.log(response);
	});


 }]).config(function($interpolateProvider, $httpProvider){
        $interpolateProvider.startSymbol('[[').endSymbol(']]');
});



