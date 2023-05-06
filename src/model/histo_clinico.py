# from config.db import db, app, ma 

# class histoclinicos(db.Model):
#     __tablename__ = "tblhistoclinicos"

    
#     id  = db.Column(db.Integer, primary_key=True)
#     paciente = db.Column(db.String(50))
#     odontologo = db.Column(db.String(50))
#     fecha = db.Column(db.Date)
#     notas = db.Column(db.String(250))
#     id_pacientes = db.Column(db.Integer,db.ForeignKey('tblpaciente.id'))
#     id_odontologos = db.Column(db.Integer,db.ForeignKey('tblodontologo.id'))

#     def __init__(self, paciente,odontologo,fecha,notas,id_pacientes,id_odontologos):
#         self.paciente = paciente
#         self.odontologo = odontologo
#         self.fecha = fecha
#         self.notas = notas
#         self.id_pacientes = id_pacientes
#         self.id_odontologos = id_odontologos


# with app.app_context():
#     db.create_all()

