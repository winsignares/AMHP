from config.db import db, app, ma 

class pacientes(db.Model):
    __tablename__ = "tblpacientes"

    
    id  = db.Column(db.Integer, primary_key=True)
    Rol = db.Column(db.String(50))
    fecha_de_regitro = db.Column(db.String(50))
    Name = db.Column(db.String(50))
    cedula = db.Column(db.Integer)
    telefono = db.Column(db.Integer)
    direccion = db.Column(db.String(50))
    Email = db.Column(db.String(50))
    fecha_nacimiento = db.Column(db.String(50))
    def __init__(self, Rol,fecha_de_regitro,Name,cedula,telefono,direccion,Email,fecha_nacimiento):
        self.Rol = Rol
        self.fecha_de_regitro = fecha_de_regitro
        self.Name = Name
        self.cedula = cedula
        self.telefono = telefono
        self.direccion = direccion
        self.Email = Email
        self.fecha_nacimiento = fecha_nacimiento
     
with app.app_context():
    db.create_all()
