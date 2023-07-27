#se importa el gestor de base de datos
from flask_sqlalchemy import SQLAlchemy

import os

def configuresSqlite(app):
    #es la ruta de la direccion absoluta donde estara la base de datos
    dbdir = "sqlite:///"+os.path.abspath(os.getcwd())+"/database.db"

    #almacena el nombre del modulo donde nos encontramos
    #configura el archivo de la base de datos
    app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app) #se hace referencia a la base de datos con la app

    return db

