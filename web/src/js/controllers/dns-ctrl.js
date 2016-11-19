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
        $scope.showDetails(data[0]);
    });

    $scope.dns = { hostname_hash: '', resolve_file_hash: '', config_file_hash: '', localip: '', remote_ip: ''};

    /* show details on click */
    $scope.showDetails = function(host) {
        $scope.details_show = true;
        $scope.detail = host;
    }

    /* Show the view to configure the valid values */
    $scope.showEdit = function() {
        $scope.details_show = false;
    }

    /* Save the view with the valid values */
    $scope.saveEdit = function() {
        console.log($scope.dns);
        $http.post('/dns_status', $scope.dns)
        .success(function(data){

        });
        //console.log($scope.hosts);
    }
}