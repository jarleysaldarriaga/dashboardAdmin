def listTask(mysql,idUser):
    query = mysql.connection.cursor()
    query.execute("SELECT * From tasks where task_asigned_to=%s",[idUser])
    
    Usuarios = query.fetchall()
    query.close()
    
    return Usuarios