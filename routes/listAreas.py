def listAreas(mysql):
    query = mysql.connection.cursor()
    query.execute("SELECT * From areas_services")
    
    Areas = query.fetchall()
    query.close()
    
    return Areas