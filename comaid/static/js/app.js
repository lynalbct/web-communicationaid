var auth_user = "";
var user_role;
var timer = 0;

$(document).ready(function(){


});


function login(){
    var username = $('#username').val();
    var password = $('#password').val();

    var data = JSON.stringify({'username':username, 'password':password});

    $.ajax({

        type:"POST",
        url:"http://localhost:5000/login",
        contentType:"application/json; charset=utf-8",
        data:data,
        dataType:"json",

        success: function(results){

            if(results.status == 'OK'){
                var token = results.token;
                //user_tk is abbrev of user_token
                document.cookie = "user_tk=" + token;
                window.location.replace('dashboard.html');
                $('#erroralert').hide();
            
            else {
            $('#erroralert').text(data.error).show();
            $('#successalert').hide(
           
        }
        },
        error: function(e){
                alert(" " + e);
        }

    });

}
}