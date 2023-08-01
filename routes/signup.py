def signup(request,mysql):
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]
    
    query = mysql.connection.cursor()
    result = query.execute("INSERT INTO users(name,username,password) values(%s,%s,%s)",(name,username,password))
    
    mysql.connection.commit()
    query.close()
    
    return result
    