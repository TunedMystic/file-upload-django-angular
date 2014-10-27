/*
    AngularJS, Django, and Jquery File-upload App.
                Sandeep Jadoonanan
*/

$(document).ready(function() {
  
  // Hide the '<input type="file">' tag and
  // emulate its click.
  $("#thefilesBrowse").click(function(e) {
    e.preventDefault();
    $("#thefiles").click();
  });
  
});