#se importa la conexion a MYSQL DEL XAMPP
from flask_mysqldb import MySQL

def mysqlConnect(app):
    
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'softdev'
    
    db=MySQL(app)
    
    return db
    
    