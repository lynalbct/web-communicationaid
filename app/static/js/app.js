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
$(document).ready(function () {
            $('#target').submit(function () {
                var username = $("#username").val();
                var password = $("#password").val();
                $.ajax({
                    url: "http://127.0.0.1:5000/api/login/",
                    contentType: 'application/json; charset=utf-8',
                    data: JSON.stringify({
                        'username': username,
                        'password': password
                    }),
                    method: "GET",
                    dataType: "json",
                    crossDomain: true,
                    headers: {
                        'Authorization' : 'Basic ' + btoa(username + ':' + password)
                    },
                    success: function(resp) {
                        if (resp.role_id == '2') {
                            alert('login success!');
                            console.log("success");
                            localStorage.setItem('token', resp.token);
                            localStorage.setItem('role_id', resp.role_id);
                            localStorage.setItem('public_id', resp.public_id);
                            localStorage.setItem('auth_id', 'Basic ' + btoa(username + ':' + password));
                            window.location.href='/visitor/landing';
                        }
                        if (resp.role_id == '1') {
                            alert('login success!');
                            console.log("success");
                            localStorage.setItem('token', resp.token);
                            localStorage.setItem('role_id', resp.role_id);
                            localStorage.setItem('public_id', resp.public_id);
                            localStorage.setItem('auth_id', 'Basic ' + btoa(username + ':' + password));
                            window.location.href='/clerk/landing';
                        }
                        if (resp.role_id == '0') {
                            alert('login success!');
                            console.log("success");
                            localStorage.setItem('token', resp.token);
                            localStorage.setItem('role_id', resp.role_id);
                            localStorage.setItem('public_id', resp.public_id);
                            localStorage.setItem('auth_id', 'Basic ' + btoa(username + ':' + password));
                            window.location.href='/admin/landing';
                        }
                    },
                    error: function () {
                        console.log('error');
                        alert('Credentials invalid!');
                        window.location.href='/login';
                    },
                    complete: function (jqXHR) {
                        if (jqXHR.status == '401') {
                            console.log(jqXHR.status)
                        }
                    }
                })
            })
        })