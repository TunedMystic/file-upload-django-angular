/*
    AngularJS, Django, and Jquery File-upload App.
                Sandeep Jadoonanan
*/

(function() {
  /*
    This app provides an interface to upload Images to the server.
  */
  
  var app = angular.module("imgApp", ["blueimp.fileupload"]);
  
  app.controller("imgUploadController", ["$scope", function($scope) {
    
    // Options to initialize the file-upload plugin.
    $scope.uploadOptions = {
      url: "/upload/",
      maxFileSize: 5000000,
      acceptFileTypes: /(\.|\/)(gif|jpe?g|png)$/i
    }
    
    // This is set to true when all files are finished uploading.
    $scope.uploadingFinished = false;
    
    // When all uploading has finished, set the 'uploadingFinished' flag to true.
    $scope.$on("fileuploadstop", function() {
      
      /*
      Files waiting to be uploaded are 'files'.
      Files that are uploaded are 'objects'.
      */
      
      var isObject = 0;
      for(var i = 0; i < $scope.queue.length; i++) {
        // If 'queue[i]' is an object.
        if($scope.queue[i].hasOwnProperty("url"))
          isObject += 1;
      }
      
      // If all the elements of the queue are objects,
      // then 'isObjects' will equal the length of $scope.queue.
      // If this is so, then all the files in the queue have been uploaded.
      if($scope.queue.length == isObject) {
        console.log("File uploading has finished.");
      $scope.uploadingFinished = true;
      }
      
    });
    
  }]);
  
  app.controller("FileDestroyController", ["$scope", "$http", function($scope, $http) {
    
    $scope.$state = function() {}
    
    $scope.$destroy = function() {}
    
    $scope.$cancel = function() {}
    
  }]);
  
})();
