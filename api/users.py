def get_users(mysql, jsonify):
    query = mysql.connection.cursor()
    query.execute('SELECT * FROM users')
    data = query.fetchall()
    query.close()
    
    return jsonify(data)

def get_users_account(mysql,jsonify):
    query = mysql.connection.cursor()
    query.execute('SELECT id,name,username,area FROM users')
    data = query.fetchall()
    query.close()
    
    return jsonify(data)

def get_user(id, mysql, jsonify):
    query = mysql.connection.cursor()
    query.execute('SELECT * FROM users where id = %s',(id))
    data = query.fetchone()
    query.close()
    
    return jsonify(data)

def update_user(id, mysql, jsonify, request):
    data = request.get_json(force=True)
    query = mysql.connection.cursor()
    
    query.execute('UPDATE users SET name = %s,username = %s, email = %s, phone = %s,role = %s,area = %s,state = %s where id = %s',(data["name"],data["username"],data["email"],data["phone"],data["role"],data["area"],data["state"],id))
    
    mysql.connection.commit()
    query.close()
    return jsonify({'message': 'Datos actualizados con exito'})