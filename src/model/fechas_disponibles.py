from config.db import db, app, ma 

class fechas_dispo(db.Model):
    __tablename__ = "tblfechadisponible"

    
    id  = db.Column(db.Integer, primary_key=True)
    fechas_dispon = db.Column(db.String(50))
    # id_pacientes = db.Column(db.Integer,db.ForeignKey('tblpaciente.id'))


    def __init__(self, fechas_dispon):
        self.fechas_dispon = fechas_dispon
    
     
with app.app_context():
    db.create_all()
