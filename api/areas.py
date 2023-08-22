def get_area(mysql, jsonify, id):
    query = mysql.connection.cursor()
    query.execute('SELECT * FROM areas_services where id = %s ', (id))
    data = query.fetchone()
    query.close()
    
    return jsonify(data)