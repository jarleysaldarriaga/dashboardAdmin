def deleteUser(request,mysql,idUserActive):
    
    id = request.form["id"]
    id = int(id)
    query = mysql.connection.cursor()
    
    if idUserActive == id:
        resulDelete = None
    else:
        resulDelete = query.execute("DELETE FROM users where id = %s",(id,))
    
        mysql.connection.commit()
        query.close()
        
        
    
    return resulDelete
        
    
    