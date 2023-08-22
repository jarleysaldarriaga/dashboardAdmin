$(document).ready(()=>{
    $("#add-new-area").click(()=>{
        var areaService = $("#new-area-service").val();

        if(areaService == ""){
            $("#message-form").text("error, tipo de daño o area sin llenar valide nuevamente");
            $("#message-form").attr("style", "color: red;")
        }else{
            $.ajax({
                type: "POST",
                url: "/home/area/addNewArea",
                data: {area_name:areaService},
                success: function(response) {
                    if (response == "200"){
                        $("#message-form").attr("style", "color: green;")
                        $("#message-form").text("Se guardo con exito");
                        setInterval(function(){
                            location.reload();
                        },1000)
                    }else if(response == "404"){
                        $("#message-form").attr("style", "color: red;")
                        $("#message-form").text("no se guardo verifique la informacion e intentelo de nuevo");
                    }
                },
                error: function(error){
                    $("#message-form").attr("style", "color: red;")
                    $("#message-form").text("no se pudo guardar intentelo nuevamente");
                } 
            });
        }
    });

    $(".btn-areas").click(function(){
        var id = $(this).data('id');
        
        $.ajax({
            url: '/api/v1/areas/'+id,
            type: 'GET',
            data:{id:id},

            success: function(res){
                var idArea = res[0];
                var nameArea = res[1];
                
                $("#modal-edit-area").show();

                $("#edit-area-id").val(idArea);
                $("#edit-area-name").val(nameArea)
                
                
            }, 
            error: function(error){
                
            }
        })
    });

    $("#cancel-close-area").click(()=>{
        $("#modal-edit-area").hide();
    });

    $("#check-update-area").click(()=>{
        var id = $("#edit-area-id").val();
        var area_name = $("#edit-area-name").val();
        if(area_name != ""){
            $.ajax({
                url: '/home/area/editArea',
                type: 'POST',
                data:{id:id, area_name:area_name},
    
                success: function(res){
                    if(res == "200"){
                        $("#message-form-area").attr("style", "color: white;")
                        $("#message-form-area").attr("class", "alert alert-success")
                        $("#message-form-area").text("Se actualizo con exito!");
                        setInterval(function(){
                            location.reload();
                        },1000)
                    }else{
                        $("#message-form-area").attr("style", "color: white;")
                        $("#message-form-area").attr("class", "alert alert-danger")
                        $("#message-form-area").text("No se pudo actualizar verifique nuevamente");
                    }
                        
                }, 
                error: function(error){
                    $("#message-form-area").attr("style", "color: white;")
                    $("#message-form-area").attr("class", "alert alert-danger")
                    $("#message-form-area").text("No se pudo actualizar comuniquese con el administrador");
                }
            })
        }else{
            $("#message-form-area").attr("style", "color: white;")
            $("#message-form-area").attr("class", "alert alert-danger")
            $("#message-form-area").text("No se pueden guardar datos sin valor");
        }
    });

    $("#check-delete-area").click(()=>{
        var id = $("#edit-area-id").val();

        $.ajax({
            url: '/home/area/deleteArea',
            type: 'DELETE',
            data:{id:id},

            success: function(res){
                if(res == "200"){
                    $("#message-form-area").attr("style", "color: white;")
                    $("#message-form-area").attr("class", "alert alert-success")
                    $("#message-form-area").text("Se elimino con exito!");
                    setInterval(function(){
                        location.reload();
                    },1000)
                }else{
                    $("#message-form-area").attr("style", "color: white;")
                    $("#message-form-area").attr("class", "alert alert-danger")
                    $("#message-form-area").text("No se pudo Eliminar verifique nuevamente");
                }
                    
            }, 
            error: function(error){
                $("#message-form-area").attr("style", "color: white;")
                $("#message-form-area").attr("class", "alert alert-danger")
                $("#message-form-area").text("No se pudo Eliminar comuniquese con el administrador");
            }
        })
    });
});