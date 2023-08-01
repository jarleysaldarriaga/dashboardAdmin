def listAccounts(mysql):
    query = mysql.connection.cursor()
    query.execute("SELECT * From users")
    
    Usuarios = query.fetchall()
    query.close()
    
    return Usuarios