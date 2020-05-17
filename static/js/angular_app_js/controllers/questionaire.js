angular.module('vidyalayData', []).controller('questionaire', [
    '$scope',
    '$http',
    function($scope, $http) {


    $scope.isSubmitted = false;
    $scope.standards = ["I","II","III","IV","V","VI","VII","VIII","IX","X"];
    $scope.divisions = ["A","B","C","D","E"];

    $scope.standard = "";
    $scope.division = "";

    function generateHomework(){
        $scope.standard = "II";
        $scope.division = "A";
        $scope.subject = "Maths";
        $scope.doh = "13-04-2020";
        $scope.name = "Sangita";
        $scope.toh = "Video";
        $scope.dessoh = "Video Homework";
    }
    //generateHomework();

    function resetHomework(){
        $scope.standard = "";
        $scope.division = "";
        $scope.subject = "";
        $scope.doh = "";
        $scope.name = "";
        $scope.toh = "";
        $scope.dessoh = "";
    }

    $scope.submitTeacher = function(isValid){
        $scope.isSubmitted = true;

        if(isValid){
            var homeworkData = {
                standard:$scope.standard,
                division:$scope.division,
                subject : $scope.subject,
                doh : $scope.doh,
                name : $scope.name,
                toh : $scope.toh,
                dessoh : $scope.dessoh
            }

            $http.post('/insert_homework', homeworkData).then(function successCallback(response) {
                var result = response.data;
                swal({
					title: "Success",
					text: "Homework Uploaded Successfully..!!",
					buttonsStyling: false,
					confirmButtonClass: "btn btn-success"

				}).catch(swal.noop);

                $scope.isSubmitted = true;
            }, function errorCallback(response) {
                 var result = response.data;
                 swal({
					title: "Error",
					text: result,
					type: 'error',
					confirmButtonClass: "btn btn-info",
					buttonsStyling: false
				   }).catch(swal.noop)
				   resetHomework();
                 $scope.isSubmitted = true;
            });
        }
        $scope.isSubmitted = true;
    }



 }]).config(function($interpolateProvider, $httpProvider){
        $interpolateProvider.startSymbol('[[').endSymbol(']]');
});



