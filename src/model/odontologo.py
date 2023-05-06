# from config.db import db, app, ma 

# class odontologos(db.Model):
#     __tablename__ = "tblodontologo"

    
#     id  = db.Column(db.Integer, primary_key=True)
#     nombre = db.Column(db.String(50))
#     direccion = db.Column(db.String(50))
#     telefono = db.Column(db.Integer)
#     correo = db.Column(db.String(50))
#     especialidad = db.Column(db.String(250))

#     def __init__(self, nombre,direccion,telefono,correo,especialidad):
#         self.nombre = nombre
#         self.direccion = direccion
#         self.telefono = telefono
#         self.correo = correo
#         self.especialidad = especialidad
    
# with app.app_context():
#     db.create_all()
