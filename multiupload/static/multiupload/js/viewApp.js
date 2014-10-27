


(function() {
  /*
    This app provides an interface to view and delete images
    stored on the server.
  */
  
   var app = angular.module("imgViewApp", ["ngCookies"]);
   
   app.run(["$http", "$cookies", function($http, $cookies) {
     // set the CSRF token here
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
   }]);
   
   app.controller("ImageViewController", ["$scope", "$http", "$cookies", function($scope, $http, $cookies) {
     $scope.message = "This controller is configured properly!";
     $scope.images = [];
     
     $scope.getImageData = function() {
      
      $http.post("/93ec8e6b7a146f7d/")
      .success(function(data, status, headers, config) {
        console.log("Success!");
        
        $scope.data = data;
        $scope.statuc = status;
        $scope.headers = headers;
        $scope.config = config;
        
        $scope.images = $scope.data["files"];
        
      })
      .error(function(data, status, headers, config) {
        console.log("Error!");
        
        $scope.data = data;
        $scope.statuc = status;
        $scope.headers = headers;
        $scope.config = config;
      });
      
     }  // getImageData
     
     // Delete the image (i) from images.
     $scope.deleteImage = function(i) {
       //$scope.$apply(function() {
       //  $scope.images[i].url = "/static/multiupload/img/loading.gif";
       //});
       $scope.images[i].url = "/static/multiupload/img/loading.gif";
       $http({
         url: $scope.images[i].deleteUrl,
         method: $scope.images[i].deleteType
       })
       .success(function(data, status, headers, config) {
         // Delete the image from the list.
         $scope.images.splice(i, 1);
       })
       .error(function(data, statuc, headers, config) {
         
       });
     }
     
     window.ss = $scope;
     
     // Get Image data when the controller has no Image data.
     if(!$scope.images.length)
       $scope.getImageData();
     
   }]);
   
})();