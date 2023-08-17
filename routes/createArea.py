def createArea(request,mysql):
    area_name = request.form["area_name"]
    
    query = mysql.connection.cursor()
    consulta = query.execute("INSERT INTO areas_services(area_name) values(%s)",[area_name])
    
    mysql.connection.commit()
    query.close()

    if consulta:
        return "success"
    else:
        return None