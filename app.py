#import library flask to use
from flask import Flask, render_template, request, make_response,session,redirect,url_for,flash
#render template renderiza las vistas correspondientes o asignadas
#request permite acceder a las funciones de envio de datos por metodos get y post
#make response
#session
#scape
#redirect se encarga de moverse entre paginas
#url_for devuelve el valor asociado al retorno del llamdo

#importar libreria para cifrar contraseñas
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
#importa la configuracion de conexion a sqlite
#from config.configuresqlite import configuresSqlite
#db = configuresSqlite(app)
from flask_mysqldb import MySQL
from database.mysqliconnect import mysqlConnect
mysql = mysqlConnect(app)

#se crea las columnas de la base de datos atravez de clases
#se importa el modelo de los usuarios con sus atributos
#from models.userModel import users
#from models.caseModel import cases
#Cases = cases(db)
#Users = users(db)
    

#appcontext permite el acceso a verificar la base de datos
#with app.app_context():
#    db.create_all()
    
#la llave secreta se necesita para poder acceder
app.secret_key = "12345"

@app.route('/usuarios')
def users():
    query = mysql.connection.cursor()
    query.execute("SELECT * FROM users")
    usuarios = query.fetchall()
    query.close()
    
    return render_template("usuarios.html",usuarios=usuarios)
#########################################################################################
request = request
session = session
redirect = redirect
url_for = url_for

from routes import login,signup as register,accounts as account, listAccounts, updateUser as userUpdate, createTask,userForArea,listTask


#########################################################################################
#esta ruta es el index y el login al mismo tiempo para obtener los datos
@app.route("/",  methods=["GET", "POST"])
def index():
    if request.method == "POST":
        login.login(request,mysql,session,redirect,url_for)
    if "username" in session:
        return redirect(url_for("home"))
    
    return render_template("index.html")
    
#esta ruta se encarga de crear los usuario
##################################################################################
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        resulSignup = register.signup(request,mysql)
        if resulSignup == 1:
            flash("Resgistro hecho exitosamente")
        else:
            flash("No se puedo registrar Intentelo nuevamente")
            
        return redirect(url_for("index"))
        
    return render_template("signup.html")
##################################################################################
@app.route("/home")
def home():
    #valida que exista la session
    if "username" in session:
        return render_template("home.html")
    #en caso de no haber session redirecciona al login
    return redirect(url_for("index"))
    #return render_template("home.html")

#####################################################################################
#asigna el valor a la cookie 
@app.route('/home/accounts', methods=["POST","GET"])
def accounts():
    #resp = make_response(render_template("home.html"))
    #resp.set_cookie("username", "stiv99")
    account.accounts(request,mysql)
    if "username" in session:
        Usuarios = listAccounts.listAccounts(mysql)
        return render_template("accounts.html",Usuarios=Usuarios)
    return redirect(url_for("index"))
    
####################################################################################

@app.route('/home/updateUser', methods=["GET", "POST"])
def updateUser():
    if request.method == "POST":
        userUpdate.updateUser(request,mysql)
        return redirect(url_for("accounts"))

####################################################################################
@app.route('/home/tasks', methods=["GET","POST"])
def tasks():
    UserId = session["id"]
    areaUser = session["area"]
    usersArea = userForArea.userForArea(mysql,areaUser)
    taskList = listTask.listTask(mysql,UserId)
    print(usersArea)
    if request.method == "POST":
        createTask.createTask(request,mysql)
        return redirect(url_for("tasks"))
    return render_template("task.html", usersArea=usersArea,taskList=taskList)

####################################################################################
@app.route('/logout')
def logout():
    session.pop("username", None)
    
    return redirect(url_for("index"))
        
####################################################################################

#main hace referencia al paquete de ejecucion principal
if __name__ == "__main__":

    #parametros de run
    app.run(debug=True, port=5000, host="192.168.18.40")
    #debug detecta los cambios automaticamente y reinicia el servidor
    #port nos permite establecer el puerto sobre el que correra la app
    #host es donde nuestra app va a correr en este caso localhost