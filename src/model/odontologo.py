from config.db import db, app, ma 

class odontologos(db.Model):
    __tablename__ = "tblodontologos"

    
    id  = db.Column(db.Integer, primary_key=True)
    Rol = db.Column(db.String(50))
    fecha_de_regitro = db.Column(db.String(50))
    nombre = db.Column(db.String(50))
    cedula = db.Column(db.Integer)
    direccion = db.Column(db.String(50))
    telefono = db.Column(db.Integer)
    correo = db.Column(db.String(50))
    especialidad = db.Column(db.String(250))
    id_admin = db.Column(db.Integer,db.ForeignKey('tbladmin.id'), nullable=True)

    def __init__(self,Rol,fecha_de_regitro, nombre,cedula,direccion,telefono,correo,especialidad,id_admin=None):
        self.Rol = Rol
        self.fecha_de_regitro = fecha_de_regitro
        self.nombre = nombre
        self.cedula = cedula
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.especialidad = especialidad
        self.id_admin = id_admin
    
with app.app_context(): 
    db.create_all()
