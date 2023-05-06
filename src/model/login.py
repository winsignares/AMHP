# from config.db import db, app, ma 

# class login(db.Model):
#     __tablename__ = "tbllogin"

    
#     id  = db.Column(db.Integer, primary_key=True)
#     usuario = db.Column(db.String(50))
#     contraseña = db.Column(db.String(50))
#     tipo_user = db.Column(db.Integer)
#     id_pacientes = db.Column(db.Integer,db.ForeignKey('tblpaciente.id'))
#     id_odontologos = db.Column(db.Integer,db.ForeignKey('tblodontologo.id'))

#     def __init__(self, usuario,contraseña,tipo_user):
#         self.usuario = usuario
#         self.contraseña = contraseña
#         self.tipo_user = tipo_user
     
# with app.app_context():
#     db.create_all()
