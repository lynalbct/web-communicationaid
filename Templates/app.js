$(document).ready(function(){
    $('form').on('submit', function(event){
    $.ajax({
        data: {
            username: $('#username').val(),
            password: $('#password').val()
        },
        type: 'GET',
        url: '/login/api'
    })
        .done(function (data)
    {

        if (data.error) {
            $('#erroralert').text(data.error).show();
            $('#successalert').hide();
        }
        else {
            window.location.replace('dashboard.html');
            $('#erroralert').hide();
        }
    });

    event.preventDefault();
    });
});