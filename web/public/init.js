(function($){
  $(function(){

    $('.sidenav').sidenav();
    $('.datepicker').datepicker();

  }); // end of document ready
})(jQuery); // end of jQuery name space

jQuery(document).ready(function(){
  jQuery('.timepicker').timepicker({
    twelveHour: false
  });
});