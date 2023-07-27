#import library flask to use
from flask import Flask, render_template, request, make_response,session,redirect,url_for
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
#esta ruta es el index y el login al mismo tiempo para obtener los datos
@app.route("/",  methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        query = mysql.connection.cursor()
        query.execute("SELECT name,username, password From users where username = %s and password = %s",(username,password))
        
        user = query.fetchone()
        query.close()

        if user:
            session["name"] = user[0]
            session["username"] = user[1]
            return redirect(url_for("home"))
        return redirect(url_for("index"))
    if "username" in session:
        return redirect(url_for("home"))
    
    #title = "Index"
    #lista = ["camilo", "tatiana", "estiverd"]
    return render_template("index.html")
    #para pasar variables y valores se envia como argumento atravez del render como variable
    
#esta ruta se encarga de crear los usuario
##################################################################################
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        username = request.form["username"]
        password = request.form["password"]
        
        query = mysql.connection.cursor()
        query.execute("INSERT INTO users(name,username,password) values(%s,%s,%s)",(name,username,password))
        
        mysql.connection.commit()
        query.close()
        
        return redirect(url_for("index"))
        
    return render_template("signup.html")
##################################################################################
@app.route("/home")
def home():
    #valida que exista la session
    if "username" in session:
        return render_template("home.html")
        #return "you are %s" % escape(session["username"])
    #en caso de no haber session redirecciona al login
    return redirect(url_for("index"))
    #return render_template("home.html")

##################################################################################
@app.route("/search/user")
def search():
    nickname = request.args.get("nickname")
    user = Users.query.filter_by(username=nickname).first()
    if user:
        return "usuario: "+ user.username + "contraseña: " +user.password
    return "property don't know"

#####################################################################################
#asigna el valor a la cookie 
@app.route('/home/accounts', methods=["POST","GET"])
def accounts():
    #resp = make_response(render_template("home.html"))
    #resp.set_cookie("username", "stiv99")
    if request.method == "POST":
        name = request.form["name"]
        username = request.form["username"]
        password = request.form["password"]
        
        query = mysql.connection.cursor()
        query.execute("INSERT INTO users(name,username,password) values(%s,%s,%s)",(name,username,password))
        
        mysql.connection.commit()
        query.close()
    
    if "username" in session:
        query = mysql.connection.cursor()
        query.execute("SELECT * From users")
        
        Usuarios = query.fetchall()
        query.close()
        return render_template("accounts.html",Usuarios=Usuarios)
    return redirect(url_for("index"))
    
####################################################################################
@app.route('/home/editUser/<string:username>',methods=["GET","POST"])
def editUser(username):
    
    query = mysql.connection.cursor()
    query.execute("SELECT * From users where username = %s ",[username])
    
    usuario=query.fetchone()
    query.close()
    
    return render_template("editUser.html",usuario=usuario)

@app.route('/home/updateUser', methods=["GET", "POST"])
def updateUser():
    if request.method == "POST":
        id = request.form["id"]
        name = request.form["name"]
        username = request.form["username"]
        email = request.form["email"]
        area = request.form["area"]
        role = request.form["role"]
        phone = request.form["phone"]
        
        query = mysql.connection.cursor()
        query.execute("UPDATE users SET  name = %s, username= %s,email=%s,phone=%s,role=%s,area=%s  where id = %s", (name,username,email,phone,role,area,id))
        
        mysql.connection.commit()
        query.close()
        
        return redirect(url_for("accounts"))


    
####################################################################################
#recupera el valor de la cookie ya asignada anteriormente
@app.route('/cookie/read')
def read_cookie():
    username = request.cookies.get("username", None)
    
    if username == None:
        return "the cookie doesn't exit."
    
    return username
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