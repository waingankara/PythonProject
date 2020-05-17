angular.module('vidyalayData', []).controller('questionaire', [
    '$scope',
    '$http',
    function($scope, $http) {

    $scope.standards = ["I","II","III","IV","V","VI","VII","VIII","IX","X"];
    $scope.standard = "0";

    $scope.divisions = ["A","B","C","D","E"];
    $scope.division = "0";

 }]).config(function($interpolateProvider, $httpProvider){
        $interpolateProvider.startSymbol('[[').endSymbol(']]');
});



