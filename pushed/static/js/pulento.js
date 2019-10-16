
    $aux = false;


    $(document).on('submit', '#post-form',function(e){
    console.log("hola gente");
    $.ajax({
        type:'POST',
        url:'seguridad',
        data:{
            old_password:$('#oldpass').val(),
            new_pass:$('#newpass').val(),
            confirm_pass:$('#confirmpass').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        },
        success:function(){
            console.log("Si funca")
            document.getElementById("post-form").reset();
            aux = true;
        },
        error: function() {
            console.log("no funco");
            aux = true; 
        }        
    });
    });

