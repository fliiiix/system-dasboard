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
        $scope.detail = host;
    }
}