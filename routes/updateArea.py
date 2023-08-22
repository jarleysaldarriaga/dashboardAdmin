def updateArea(request,mysql):

    id = request.form["id"]
    area_name = request.form["area_name"]
    
    
    query = mysql.connection.cursor()
    query.execute("UPDATE areas_services SET  area_name = %s where id = %s", (area_name,id))
    
    mysql.connection.commit()
    query.close()

    if query:
        return "success"
    else:
        return None