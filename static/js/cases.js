$(document).ready(()=>{

    $("#new-case-areaAsigned").change(function(){

        var areaDamage = $("#new-case-areaAsigned").val();
        var select = $("#newCaseDamage");

        if(areaDamage == ""){
            select.empty();
            var option = $("<option>", {
                value: "",
                text: "Esperando area de asignacion..."
            });
            $("#newCaseDamage").append(option);
        }
        

        $.ajax({
            url: "/api/v1/damages/areaDamages/"+areaDamage,
            type: "GET",
            data: {areaD:areaDamage},

            success: function (response) {
                select.empty();
                if(response.length > 0){
                    response.forEach(function(element){
                        var option = $("<option>", {
                            value: element[0],
                            text: element[1]
                        });
                        $("#newCaseDamage").append(option);
                    });
                }else{
                    var option = $("<option>", {
                        value: "",
                        text: "No hay tipo de solicitud para esta area"
                    });
                    $("#newCaseDamage").append(option);
                }
                
            }
        });

        
    });
});