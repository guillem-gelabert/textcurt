$(document).ready(function() {
  $(window).scroll(function() {
    if ($(this).scrollTop() > 75) {
      $("#menu").fadeOut(100);
    } else {
      $("#menu").fadeIn(100);
    }
  });

  $(document).scroll(function(){

    var window_height = $(window).height()
    var document_height = $(document).height()
    var remaining_time = $(document).scrollTop() / (document_height - window_height) * 100;
    $("#groc").css("width", remaining_time + "%");
  });
});
