from config.db import db, app, ma 

class admins(db.Model):
    __tablename__ = "tbladmin"

    
    id  = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50))
    contraseña = db.Column(db.String(50))
    # tipo_user = db.Column(db.Integer)
    id_citas= db.Column(db.Integer,db.ForeignKey('tblcitas.id'))

    def __init__(self, usuario,contraseña):
        self.usuario = usuario
        self.contraseña = contraseña
        # self.tipo_user = tipo_user
     
with app.app_context():
    db.create_all()
