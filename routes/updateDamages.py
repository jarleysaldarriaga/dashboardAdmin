def updateDamages(request,mysql):

    id = request.form["id"]
    typeDamage = request.form["typeDamage"]
    areaDamage = request.form["areaDamage"]
    
    
    query = mysql.connection.cursor()
    query.execute("UPDATE type_damage SET  typeDamage = %s, areaDamage= %s where id = %s", (typeDamage,areaDamage,id))
    
    mysql.connection.commit()
    query.close()

    if query:
        return "200"
    else:
        return "404"