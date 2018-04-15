
function edit_parent() {

	$.ajax(
		{
			url: 'http://127.0.0.1:5000/edit_parent/<int:acc_id>',
			contentType: 'application/json; charset=utf-8',
			data: JSON.stringify({
				'fname_p': $("#fname_p").val(),
				'lname_p': $("#lname_p").val(),
				'bday_p': $("#bday_p").val(),
				'add_p': $("#add_p").val()
			}),
			type: "POST",
			dataType: "json",
			error: function (e) {
			},
			success: function (resp) {
                if (resp.status == 'ok') {
                	alert("Successfully updated!")
                    window.location.replace('childinfo.html')

                 }
				else {
					alert("ERROR")
				}

			}
		});
}

function getinfo_parent(acc_id){

	 $("#parent").show();
	 alert('hey!!')

    $.ajax({
    		url: 'http://127.0.0.1:5000/parent/'+acc_id,
    		type: "GET",
    		dataType: "json",
    		success: function(resp) {

				if (resp.status  == 'ok') {
				   for (i = 0; i < resp.count; i++)
                                  {
									   fname_p = resp.entries[i].fname_p;
									   lname_p = resp.entries[i].lname_p;
									   bday_p = resp.entries[i].bday_p;
									   add_p = resp.entries[i].add_p;
                                       $("#parent").append(parent(fname_p,lname_p, bday_p, add_p));

                                  }



				} else
				{
                                       $("#parent").html("");
					alert(resp.message);
				}
    		}
		});
}

function parent(fname_p,lname_p,bday_p,add_p)
{
   return '<div class="col-md-12 col-sm-12 col-xs-12">' +
       '<p>First Name: '+ ' ' +fname_p+  '</p>'+
       '<p>Last Name:'+ ' ' +lname_p+ '</p>'+
       '<p>Birthdate:'+ ' ' +bday_p+ '</p>'+
       '<p>Age:'+ ' ' +add_p+ '</p>'+
       '</div>'
}
