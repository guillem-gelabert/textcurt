$(document).ready(function() {
  $(window).scroll(function() {
    if ($(document).scrollTop() > 75) {
      $("header").removeClass("large").addClass("small");
    } else {
      $("header").removeClass("small").addClass("large");
    };
  });

  $(document).scroll(function(){
    var window_height = $(window).height();
    var document_height = $(document).height();
    var remaining_time = ($(document).scrollTop() / (document_height - window_height) * 100).toFixed(2);
    var remaining_min = (parseInt($("h3").html()) * (100-remaining_time) / 100).toFixed(0);

    if (remaining_min < 1) {
      $("#percentage").text("Fertig!");
    } else if (remaining_min == 1) {
      $("#percentage").text("Es verbleibt eine Leseminute");
    } else {
      $("#percentage").text("Es verbleiben " + remaining_min + " Leseminuten");
    };

    $("#groc").css("width", remaining_time + "%");
  });
});
