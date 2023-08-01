def login(request,mysql,session,redirect,url_for):
    
    username = request.form["username"]
    password = request.form["password"]
    
    query = mysql.connection.cursor()
    query.execute("SELECT id,name,username, password,area From users where username = %s and password = %s",(username,password))
    
    user = query.fetchone()
    query.close()

    if user:
        session["id"] = user[0]
        session["name"] = user[1]
        session["username"] = user[2]
        session["area"] = user[4]
        return redirect(url_for("home"))
    return redirect(url_for("index"))

    