def deleteDamage(request,mysql,id):
    
    id = request.form["id"]
    query = mysql.connection.cursor()
    
    resulDelete = query.execute("DELETE FROM type_damage where id = %s",(id,))

    mysql.connection.commit()
    query.close()
        
    if resulDelete:
        return "200"
    else:
        return "404"
        