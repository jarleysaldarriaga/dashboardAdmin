$(document).ready(function(){
    $("#modal-editUser-close").click(function(){
        $("#modal-edit-user").hide();
    })
    
    $(".btn-datos").click(function(){
        var id = $(this).data('id');
        var name = $(this).data('name');
        var user = $(this).data('user');
        var email = $(this).data('email');
        var phone = $(this).data('phone');
        var role = $(this).data('role');
        var area = $(this).data('area');

        $.ajax({
            url: '/home/accounts',
            type: 'GET',
            data:{id:id},

            success: function(res){
                $("#modal-edit-user").show();
                $("#editId").val(id);
                $("#editName").val(name);
                $("#editUser").val(user);
                $("#editEmail").val(email);
                $("#editPhone").val(phone);
                $("#editRole").val(role);
                $("#editArea").val(area);
            }, 
            error: function(error){
                console.log(error)
            }
        })
    })

    $("#update-account-user").click(function(){
        var id = $("#editId").val();
        var name =$("#editName").val();
        var user =$("#editUser").val();
        var email = $("#editEmail").val();
        var phone = $("#editPhone").val();
        var role = $("#editRole").val();
        var area = $("#editArea").val();
        
        $.ajax({
            url: '/home/updateUser',
            type: 'POST',
            data:{id:id,name:name,username:user,email:email,phone:phone, role:role, area:area},

            success: function(res){
                $("#modal-edit-user").hide();
                location.reload();
            }, 
            error: function(error){
                console.log(error)
            }
        })
    })
});