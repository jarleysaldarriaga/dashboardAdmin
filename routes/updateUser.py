def updateUser(request,mysql):
    id = request.form["id"]
    name = request.form["name"]
    username = request.form["username"]
    email = request.form["email"]
    area = request.form["area"]
    role = request.form["role"]
    phone = request.form["phone"]
    
    query = mysql.connection.cursor()
    query.execute("UPDATE users SET  name = %s, username= %s,email=%s,phone=%s,role=%s,area=%s  where id = %s", (name,username,email,phone,role,area,id))
    
    mysql.connection.commit()
    query.close()