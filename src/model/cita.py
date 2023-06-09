from config.db import db, app, ma


class citas(db.Model):
    __tablename__ = "tblcitas"

    id = db.Column(db.Integer, primary_key=True)
    Rol = db.Column(db.String(50))
    consulta = db.Column(db.String(50))
    tarje_tade_credito = db.Column(db.String(50))
    Num_tarjeta = db.Column(db.String(50))
    estado_citas = db.Column(db.String(250))
    problema = db.Column(db.String(250))
    id_paciente = db.Column(db.Integer,db.ForeignKey('tblpacientes.id'))
    id_odontologos = db.Column(db.Integer,db.ForeignKey('tblodontologos.id'))
    id_fechadispo = db.Column(db.Integer,db.ForeignKey('tblfechadisponible.id'))
    

    def __init__(self,Rol,consulta,tarje_tade_credito, Num_tarjeta,estado_citas,problema,id_paciente,id_odontologos,id_fechadispo):
      
        self.Rol = Rol
        self.consulta = consulta 
        self.tarje_tade_credito = tarje_tade_credito
        self.Num_tarjeta = Num_tarjeta
        self.estado_citas = estado_citas
        self.problema = problema
        self.id_paciente = id_paciente
        self.id_odontologos = id_odontologos
        self.id_fechadispo = id_fechadispo
       
    
 


with app.app_context():
    db.create_all()
