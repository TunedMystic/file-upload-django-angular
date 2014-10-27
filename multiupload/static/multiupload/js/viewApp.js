/*
    AngularJS, Django, and Jquery File-upload App.
                Sandeep Jadoonanan
*/

(function() {
  /*
    This app provides an interface to view and delete images
    stored on the server.
  */
  
   var app = angular.module("imgViewApp", ["ngCookies", "ngAnimate"]);
   
   app.run(["$http", "$cookies", function($http, $cookies) {
     // set the CSRF token for requests here.
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
   }]);
   
   app.controller("ImageViewController", ["$scope", "$http", "$cookies", function($scope, $http, $cookies) {
     $scope.images = [];
     $scope.wasLoaded = false;
     $scope.occupied = true;
     
     $scope.getImageData = function() {
      
      // Make a POST request to get all Image data.
      $http.post("/93ec8e6b7a146f7d/")
      .success(function(data, status, headers, config) {
        console.log("Success!");
        
        $scope.data = data;
        $scope.images = $scope.data["files"];
        $scope.wasLoaded = true;
        
      })
      .error(function(data, status, headers, config) {
        console.log("Error!");
      });
      
     }  // getImageData
     
     // Delete the image (i) from images.
     $scope.deleteImage = function(i) {
         
       // Make a request to the 'delete image' url.
       $http({
         url: $scope.images[i].deleteUrl,
         method: $scope.images[i].deleteType
       })
       .success(function(data, status, headers, config) {
         // Remove the image from the array.
         $scope.images.splice(i, 1);
         // Check if the images array is empty.
         if($scope.images.length == 0)
           $scope.occupied = false;
       })
       .error(function(data, status, headers, config) {
         $scope.images[i].url = "/static/multiupload/img/Error_500.png";
       });
     }
     
     // Get Image data when the controller has no Image data
     // and if data was never loaded before.
     if(!$scope.images.length && !$scope.wasLoaded)
       $scope.getImageData();
       //var i = 0;
     
   }]);
   
})();
