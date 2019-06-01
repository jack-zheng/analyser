
// regist reload member list to navigation button - prev and next
$('.member_list').on('click', '.reloadbtn', function(){
    var pnum = $(this).attr('page_num');
  $(
    $.ajax({
      url: "paginate/" + pnum,
      cache: false
    }).done(function(html) {
      $(".member_list").html(html);
    })
  );
});

$("#jstest").click(function() {
    var pnum = $('#Next').attr('page_num')
    $("#233").html(pnum);
});

