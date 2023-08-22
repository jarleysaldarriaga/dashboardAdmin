def get_damages(mysql, jsonify):
    query = mysql.connection.cursor()
    query.execute('SELECT * FROM type_damage')
    data = query.fetchall()
    query.close()
    
    return jsonify(data)

def get_damage(mysql, jsonify, id):
    query = mysql.connection.cursor()
    query.execute('SELECT * FROM type_damage where id = %s ', [id])
    data = query.fetchone()
    query.close()
    
    return jsonify(data)


def get_id(mysql, jsonify,typeD,areaD):
    query = mysql.connection.cursor()
    query.execute('SELECT id FROM type_damage where typeDamage = %s,areaDamage = %s ', (typeD, areaD))
    data = query.fetchone()
    query.close()
    
    return jsonify(data)

def get_areaDamage(mysql, jsonify, areaD):
    query = mysql.connection.cursor()
    query.execute('SELECT * FROM type_damage where areaDamage = %s ', [areaD])
    data = query.fetchall()
    query.close()
    
    return jsonify(data)
    