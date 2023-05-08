# from config.db import db, app, ma 

# class pacientes(db.Model):
#     __tablename__ = "tblpaciente"

    
#     id  = db.Column(db.Integer, primary_key=True)
#     nombre = db.Column(db.String(50))
#     direccion = db.Column(db.String(50))
#     telefono = db.Column(db.Integer)
#     correo = db.Column(db.String(50))
#     fecha_nacimiento = db.Column(db.String(50))

#     def __init__(self, nombre,direccion,telefono,correo,fecha_nacimiento):
#         self.nombre = nombre
#         self.direccion = direccion
#         self.telefono = telefono
#         self.correo = correo
#         self.fecha_nacimiento = fecha_nacimiento
    
# with app.app_context():
#     db.create_all()
