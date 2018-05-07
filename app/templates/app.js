function edit_parent() {
    $.ajax({
        url: 'http://127.0.0.1:5000/edit_parent',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify({
        }),
        type: "POST",
        dataType: "json",
        success: function (resp) {

        }
    });
}
function login() {

  $.ajax(
    {
      url: 'http://mighty-badlands-16603/api/login',
      contentType: 'application/json; charset=utf-8',
      data: JSON.stringify({
        'username': $("#username").val(),
        'password': $("#password").val()
      }),
      type: "POST",
      dataType: "json",
      crossDomain: true,
      headers: {'Authorization' : 'Basic ' + btoa(username + ':' + password)},
      error: function (e) {
      },
      success: function (resp) {
        if (resp.status == 'ok') {
          localStorage.setItem('token', resp.token);
          window.location.replace('mode.html?username='+resp.message+'/');

        }
        else {
          alert(resp.message)
        }
      }
    });
}