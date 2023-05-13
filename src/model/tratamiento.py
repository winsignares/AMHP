from config.db import db, app, ma 

class tratamientos(db.Model):
    __tablename__ = "tbltratamientos"

    
    id  = db.Column(db.Integer, primary_key=True)
    paciente = db.Column(db.String(50))
    odontologo = db.Column(db.String(50))
    fecha = db.Column(db.Date)
    precio = db.Column(db.Integer)
    notas = db.Column(db.Text)
    id_citas = db.Column(db.Integer,db.ForeignKey('tblcitas.id'))

    def __init__(self, paciente,odontologo,fecha,precio,notas):
        self.paciente = paciente
        self.odontologo = odontologo
        self.fecha = fecha
        self.precio = precio
        self.notas = notas
        


with app.app_context():
    db.create_all()

