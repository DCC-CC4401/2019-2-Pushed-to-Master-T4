 function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    
    reader.onload = function(e) {
      $('#preview').attr('src', e.target.result);
    }
    
    reader.readAsDataURL(input.files[0]);
  }
}

$("#foto").change(function() {
  readURL(this);
});


	$(document).on('submit', '#regis',function(e){
			    e.preventDefault();
			    var data = new FormData();
			    data.append('csrfmiddlewaretoken',$('input[name=csrfmiddlewaretoken]').val());
			    data.append('email',$('#email').val());
			    data.append('first_name',$('#first_name').val());
				data.append('last_name',$('#last_name').val());
				data.append('password1',$('#password1').val());
				data.append('password2',$('#password2').val());
				data.append('image',$('#foto')[0].files[0]);
				data.append('registrar',$('#registrar').val());

			    for (var value of data.values()) {
				   console.log(value); 
				}
			    for (var value of data.keys()) {
				   console.log(value); 
				}
			    $.ajax({
			        type:'POST',
			        url:'registrar',
			        data: data,
					processData: false,
                	contentType: false,
			        success:function(data){
			        	console.log(data);
			            $("#emailError").html(data.email);

			            if(data == '')
			            	window.location.href = "/";

			            for (var i = data.password2.length - 1; i >= 0; i--) {
			            	if (data.password2[i] == "The password is too similar to the first name.") {
			            		data.password2[i] = "La contraseña no debe ser parecida al nombre.";
			            	}
			            	else if (data.password2[i] == "This password is too common."){
			            		data.password2[i] = "La contraseña ingresada es demasiado común.";
			            	}
			            	else if (data.password2[i] == "The two password fields didn't match."){
			            		data.password2[i] = "Las contraseñas ingresadas no coinciden.";
			            	}
							else if (data.password2[i] == "The password is too similar to the last name."){
								data.password2[i] = "La contraseña no debe ser parecida al apellido.";
							}

			            	$("#passwordError").append(data.password2[i]+"<br />").delay(9000).queue(function() {
							   $(this).html('')
							});
			            }

			            $('#regis')[0].reset();
			            $('.alert').fadeIn();
						$('.close').click(function(){
					    	$('.alert').fadeOut();
					    });				            
			            $('.alert').delay(8000).fadeOut();


			        },
			        error: function() {
			            console.log("no funco");
			        }        
			    });
			});