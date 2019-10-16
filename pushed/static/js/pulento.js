$(document).on('submit', '#post-form',function(e){
    e.preventDefault();
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
        },
        error: function() {
            console.log("no funco");
        }        
    });
});

