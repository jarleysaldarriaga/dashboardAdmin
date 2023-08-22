def deleteArea(request,mysql):
    
    id = request.form["id"]
    query = mysql.connection.cursor()
    
    resulDelete = query.execute("DELETE FROM areas_services where id = %s",(id,))

    mysql.connection.commit()
    query.close()
        
    if resulDelete:
        return "success"
    else:
        return None
        