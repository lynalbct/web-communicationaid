function login() {
    $.ajax({
        data: {
            username: $('#username').val(),
            password: $('#password').val()
        },
        type: 'POST',
        url: '/index'
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

}
function signup() {

	$.ajax(
		{
			url: 'http://127.0.0.1:5000/login',
			contentType: 'application/json; charset=utf-8',
			data: JSON.stringify({
				'username': $("#username").val(),
				'password': $("#password").val()
			}),
			type: "POST",
			dataType: "json",
			error: function (e) {
			},
			success: function (resp) {
				if (resp.status == 'ok') {
					window.location.replace('dashboard.html='+resp.message+'/');
				}
				else {
					alert(resp.message)
				}

			}
		});
}
