// Ajax para el cambio de clave, muestro una alerta con el error del formulario

$(document).on('submit', '#post-form',function(e){
    e.preventDefault();
    var data = new FormData();
    data.append('csrfmiddlewaretoken',$('input[name=csrfmiddlewaretoken]').val());
    data.append('new_password',$('#newpass').val());
    data.append('old_password',$('#oldpass').val());
    data.append('confirm_password',$('#confirmpass').val());
    $.ajax({
        type:'POST',
        url:'seguridad',
        data: data,
        processData: false,
        contentType: false,
        success:function(data){
            console.log("Si funca")
            document.getElementById("post-form").reset();
            $("#passwordError").html(data);
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

