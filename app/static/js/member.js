// csrf token for Ajax request
var csrf_token = "{{ csrf_token() }}";
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (
            !/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) &&
            !this.crossDomain
        ) {
            xhr.setRequestHeader("X-CSRFToken", csrf_token);
        }
    }
});


// regist reload member list to navigation button - prev and next
$('.member_list').on('click', '.reloadbtn', function () {
    var pnum = $(this).attr('page_num');
    $(
        $.ajax({
            url: "paginate/" + pnum,
            cache: false
        }).done(function (html) {
            $(".member_list").html(html);
        })
    );
});

// regist remove action to memeber list table
$('.member_list').on('click', '.glyphicon-remove', function () {
    var row_tr = $(this).closest('tr');
    var uid = $(this).attr('uid')
    $(
        $.ajax({
            method: "POST",
            url: "delete/" + uid,
            cache: false
        }).done(function (html) {
            // remove from UI
            row_tr.remove();
        })
    );

});

// regist copy action to memeber list table
$('.member_list').on('click', '.glyphicon-copy', function () {
    var row_tr = $(this).closest('tr')[0];
    var el = document.createElement('textarea');
    el.value = row_tr.children[2].textContent;
    // Set non-editable to avoid focus and move outside of view
    el.setAttribute('readonly', '');
    el.style = { position: 'absolute', left: '-9999px' };
    document.body.appendChild(el);
    // Select text inside element
    el.select();
    // Copy text to clipboard
    document.execCommand('copy');
    // Remove temporary element
    document.body.removeChild(el);
});

// regist remove action to memeber list table
$('.member_list').on('click', '.glyphicon-edit', function () {
    // change UI on fly
    var uname = $(this).closest('tr').find('td:eq(1)').text()
    var email = $(this).closest('tr').find('td:eq(2)').text()
    $(this).closest('tr').find('td:eq(1)').html('<input/>');
    $(this).closest('tr').find('td:eq(2)').html('<input value="' + email + '"/>');
    var save_span = '<span class="glyphicon glyphicon-save" aria-hidden="true" title="Save"></span>'
    $(this).closest('tr').find('td:eq(3)').html(save_span);

    // give username input value and give a focus
    $('.member_list').find('input').first().focus().val(uname);
});

// regist update action to memeber list table
// get uid, uname and email from row send request to update
// if update success udpate the input to txt
$('.member_list').on('click', '.glyphicon-save', function () {
    var row_update = $(this).closest('tr')[0];
    var uid = $(this).closest('tr').find('td:eq(0)').text().trim();
    var uname = $(this).closest('tr').find('input').eq(0).val();
    var email = $(this).closest('tr').find('input').eq(1).val();

    $(
        $.ajax({
            method: "POST",
            contentType: "application/json",
            url: "update",
            data: JSON.stringify({ id: uid, username: uname, email: email}),
            dataType: "json",
            cache: false
        }).done(function (data) {
            console.log(data['id']);
            $('tr:contains("'+ data['id'] +'")').find('td:eq(1)').html(data['username']);
            $('tr:contains("'+ data['id'] +'")').find('td:eq(2)').html(data['email']);
            var save_span = '<span class="label label-success">Success</span>';
            $('tr:contains("'+ data['id'] +'")').find('td:eq(3)').html(save_span);
        })
    );
});