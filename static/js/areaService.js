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
});