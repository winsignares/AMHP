from config.db import db, app, ma 

class odontologos(db.Model):
    __tablename__ = "tblodontologos"

    
    id  = db.Column(db.Integer, primary_key=True)
    Rol = db.Column(db.String(50))
    fecha_de_regitro = db.Column(db.String(50))
    nombre = db.Column(db.String(50))
    direccion = db.Column(db.String(50))
    telefono = db.Column(db.Integer)
    correo = db.Column(db.String(50))
    especialidad = db.Column(db.String(250))

    def __init__(self,Rol,fecha_de_regitro, nombre,direccion,telefono,correo,especialidad):
        self.Rol = Rol
        self.fecha_de_regitro = fecha_de_regitro
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.especialidad = especialidad
    
with app.app_context():
    db.create_all()
