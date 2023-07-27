
def users(db):
    class Users(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(80), unique=True, nullable=False)
        username = db.Column(db.String(50), unique=True, nullable=False)
        password = db.Column(db.String(80),  nullable=False)
        email = db.Column(db.String(100), unique=True)
        phone = db.Column(db.String(30), unique=True)
        role = db.Column(db.String(20))
        area = db.Column(db.String(100))
        #nullable es que no pueden estar vacios
        
        

        
    return Users