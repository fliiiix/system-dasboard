/**
 * DNS Controller
 */

angular.module('RDash')
    .controller('Dns', ['$scope', '$http', Dns]);

function Dns($scope, $http) {
    /* init data */
    $scope.hosts = [];
    $http.get('/dns_status')
    .success(function(data){
        $scope.hosts = data;
        $scope.detail = data[0];
    });

    /* show details on click */
    $scope.showDetails = function(host) {
        console.log(host);
        $scope.details_show = true;
        $scope.detail = host;
    }

    /* Show the view to configure the valid values */
    $scope.showEdit = function() {
        console.log("logloglog");
        $scope.details_show = false;
    }
}