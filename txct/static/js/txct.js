$(document).ready(function() {
  $(window).scroll(function() {
    if ($(this).scrollTop() > 75) {
      $("#menu").fadeOut(100);
    } else {
      $("#menu").fadeIn(100);
    }
  });
  $("#conte").load("senyoretes.html");
});
