def cases(db):
    class Cases(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        solicitante = db.Column(db.String(50), nullable=False)
        descripcion = db.Column(db.String(50), nullable=False)
        area_solicitud = db.Column(db.String(50), nullable=False)
        nivel_priodidad = db.Column(db.Integer)
        estado = db.Column(db.String(50), nullable=False)
    return Cases 