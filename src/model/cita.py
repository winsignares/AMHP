from config.db import db, app, ma 

class citas(db.Model):
    __tablename__ = "tblcitas"

    
    id  = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date)
    duracion = db.Column(db.Time)
    precio = db.Column(db.Integer)
    id_paciente = db.Column(db.Integer,db.ForeignKey('tblpaciente.id'))
    id_odontologo = db.Column(db.Integer,db.ForeignKey('tblodontologo.id'))

    def __init__(self, fecha,duracion,precio,id_paciente,id_odontologo):
        self.fecha = fecha
        self.duracion = duracion
        self.precio = precio
        self.id_paciente = id_paciente
        self.id_odontologo = id_odontologo
    
with app.app_context():
    db.create_all()

class citasSchema(ma.Schema):
    class Meta:
        fields = ('id','fecha','duracion','precio','id_paciente','id_odontologo')
