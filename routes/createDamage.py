def createDamage(request,mysql):
    typeDamage = request.form["typeDamage"]
    areaDamage = request.form["areaDamage"]
    
    
    query = mysql.connection.cursor()
    consulta = query.execute("INSERT INTO type_damage(typeDamage,areaDamage) values(%s,%s)",(typeDamage,areaDamage))
    
    mysql.connection.commit()
    query.close()

    if consulta:
        return "success"
    else:
        return None
    