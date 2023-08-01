def userForArea(mysql,area):
    query = mysql.connection.cursor()
    query.execute("SELECT id,name From users where area=%s ",[area])
    
    usersArea = query.fetchall()
    query.close()
    return usersArea