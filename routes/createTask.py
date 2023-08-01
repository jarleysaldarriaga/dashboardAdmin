def createTask(request,mysql):
    title = request.form["title"]
    description = request.form["description"]
    date = request.form["date"]
    user = request.form["user_asigned"]
    state = "ABIERTA"
    
    query = mysql.connection.cursor()
    consulta = query.execute("INSERT INTO tasks(title,description,date_finish,state,task_asigned_to) values(%s,%s,%s,%s,%s)",(title,description,date,state,user))
    
    mysql.connection.commit()
    query.close()
    
    print(consulta)