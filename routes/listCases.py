def asignedCase(mysql):
    query = mysql.connection.cursor()
    query.execute("SELECT * From cases where user_asignated = 'SIN ASIGNAR' ");
    
    Casos = query.fetchall()
    query.close()
    
    return Casos