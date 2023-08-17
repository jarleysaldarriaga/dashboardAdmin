$(document).ready(()=>{
    $("#add-new-damage").click(()=>{
        var typeDamage = $("#new-damage-type").val();
        var areaDamage = $("#new-area-damage").val();

        if(typeDamage == "" || areaDamage == ""){
            $("#message-form").text("error, tipo de daño o area sin llenar valide nuevamente");
            $("#message-form").attr("style", "color: red;")
        }else{
            $.ajax({
                type: "POST",
                url: "/home/cases/addNewDamage",
                data: {typeDamage:typeDamage,areaDamage:areaDamage},
                success: function(response) {
                    if (response == "200"){
                        $("#message-form").attr("style", "color: green;")
                        $("#message-form").text("Se guardo con exito");
                        setInterval(function(){
                            location.reload();
                        },1000)
                    }else if(response == "404"){
                        $("#message-form").attr("style", "color: green;")
                        $("#message-form").text("no se guardo verifique la informacion e intentelo de nuevo");
                    }
                },
                error: function(error){
                    $("#message-form").attr("style", "color: green;")
                    $("#message-form").text("no se pudo guardar intentelo nuevamente");
                } 
            });
            
        }
    })

    $(".btn-damages").click(function(){
        var id = $(this).data('id');

        $.ajax({
            url: '/api/v1/damages/'+id,
            type: 'GET',
            data:{id:id},

            success: function(res){
                var idDamage = res[0];
                var typeDamage = res[1];
                var areaDamage = res[2];
                $("#modal-edit-damage").show();

                $("#edit-damage-id").val(idDamage);
                $("#edit-damage-type").val(typeDamage)
                $("#edit-area-damage").val(areaDamage)
                
            }, 
            error: function(error){
                
            }
        })
        
    });

    $("#cancel-close-damage").click(function(){
        $("#modal-edit-damage").hide();
    });

    $("#check-update-damage").click(function(){
        var idDamage = $("#edit-damage-id").val();
        var typeDamage = $("#edit-damage-type").val();
        var areaDamage = $("#edit-area-damage").val();
        $.ajax({
            url: '/home/damages/editDamage',
            type: 'POST',
            data:{id:idDamage,typeDamage:typeDamage,areaDamage:areaDamage},

            success: function(res){
                if (res == "200"){
                    $("#message-form-damages").attr("style", "color: white;")
                    $("#message-form-damages").attr("class", "alert alert-success")
                    $("#message-form-damages").text("Se Actualizo con exito");
                    setInterval(function(){
                        location.reload();
                    },1000)
                }else if(res == "404"){
                    $("#message-form-damages").attr("style", "color: white;")
                    $("#message-form-damages").attr("class", "alert alert-danger")
                    $("#message-form-damages").text("no se Actualizo verifique la informacion e intentelo de nuevo");
                }

                setInterval(function(){
                    location.reload();
                },1000)
            }, 
            error: function(error){
                $("#message-form-damages").attr("style", "color: red;")
                $("#message-form-damages").text("no se Actualizo comuniquese con el administrador del sistema");
            }
        })
    });

    $("#check-delete-damage").click(function(){
        var idDamage = $("#edit-damage-id").val();
        
        $.ajax({
            url: '/home/damages/deleteDamage/'+idDamage,
            type: 'DELETE',
            data:{id:idDamage},

            success: function(res){
                if (res == "200"){
                    $("#message-form-damages").attr("style", "color: white;")
                    $("#message-form-damages").attr("class", "alert alert-success")
                    $("#message-form-damages").text("Se Elimino con exito");
                    setInterval(function(){
                        location.reload();
                    },1000)
                }else if(res == "404"){
                    $("#message-form-damages").attr("style", "color: white;")
                    $("#message-form-damages").attr("class", "alert alert-danger")
                    $("#message-form-damages").text("no se Elimino verifique la informacion e intentelo de nuevo");
                }

                setInterval(function(){
                    location.reload();
                },1000)
            }, 
            error: function(error){
                $("#message-form-damages").attr("style", "color: red;")
                $("#message-form-damages").text("no se Elimino comuniquese con el administrador del sistema");
            }
        })
    });


});