def accounts(request,mysql):
    if request.method == "POST":
        name = request.form["name"]
        username = request.form["username"]
        password = request.form["password"]
        
        query = mysql.connection.cursor()
        query.execute("INSERT INTO users(name,username,password) values(%s,%s,%s)",(name,username,password))
        
        mysql.connection.commit()
        query.close()
        
    if request.method == "GET":
        id = request.args.get("id")    
        
        query = mysql.connection.cursor()
        query.execute("select * from users where id = %s", (id,))
        
        usuarioEdit = query.fetchone()
        query.close()
        #print(usuarioEdit)