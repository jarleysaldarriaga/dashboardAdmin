def listDamages(mysql):
    query = mysql.connection.cursor()
    query.execute("SELECT * From type_damage");
    
    Damages = query.fetchall()
    query.close()
    
    return Damages