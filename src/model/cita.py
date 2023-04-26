from config.db import db, app, ma 

class citas(db.Model):
    __tablename__ = "tblcitas"

    
    id  = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String(50))
    edad = db.Column(db.Integer)
    genereo = db.Column(db.String(50))
    fecha = db.Column(db.Date)
    consulta = db.Column(db.String(50))
    tarje_tade_credito = db.Column(db.Date)
    numero_de_tarjeta = db.Column(db.Integer)
    id_paciente = db.Column(db.Integer,db.ForeignKey('tblpaciente.id'))
    id_odontologo = db.Column(db.Integer,db.ForeignKey('tblodontologo.id'))

    def __init__(self, nombre_completo,edad,genereo,fecha,consulta,tarje_tade_credito,id_paciente,id_odontologo):
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.genereo = genereo
        self.fecha = fecha
        self.consulta = consulta
        self.tarje_tade_credito = tarje_tade_credito
        self.id_paciente = id_paciente
        self.id_odontologo = id_odontologo
    
with app.app_context():
    db.create_all()

class citasSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre_completo','edad','genereo','fecha','consulta' ,'tarje_tade_credito','id_paciente','id_odontologo')
