from config.db import db, app, ma 

class histoclinicos(db.Model):
    __tablename__ = "tblhistoclinicos"

    
    id  = db.Column(db.Integer, primary_key=True)
    paciente = db.Column(db.String(50))
    odontologo = db.Column(db.String(50))
    fecha = db.Column(db.Date)
    notas = db.Column(db.String(250))
    id_pacientes = db.Column(db.Integer,db.ForeignKey('tblpacientes.id'))
    id_odontologos = db.Column(db.Integer,db.ForeignKey('tblodontologos.id'))

    def __init__(self, paciente,odontologo,fecha,notas):
        self.paciente = paciente
        self.odontologo = odontologo
        self.fecha = fecha
        self.notas = notas
       


with app.app_context():
    db.create_all()

