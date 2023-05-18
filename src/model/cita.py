from config.db import db, app, ma


class citas(db.Model):
    __tablename__ = "tblcitas"

    id = db.Column(db.Integer, primary_key=True)
    Nombre_completo = db.Column(db.String(50))
    Edad = db.Column(db.String(50))
    genero = db.Column(db.String(50))
    fecha = db.Column(db.String(50))
    consulta = db.Column(db.String(50))
    tarje_tade_credito = db.Column(db.String(50))
    Num_tarjeta = db.Column(db.String(50))
    problema = db.Column(db.String(250))
    estado_citas = db.Column(db.String(250))
    id_paciente = db.Column(db.Integer,db.ForeignKey('tblpacientes.id'))
    id_odontologos = db.Column(db.Integer,db.ForeignKey('tblodontologos.id'))
    

    def __init__(self, Nombre_completo, Edad,genero,fecha,consulta,tarje_tade_credito, Num_tarjeta,problema,estado_citas):
        self.Nombre_completo = Nombre_completo
        self.Edad = Edad
        self.genero = genero
        self.fecha = fecha
        self.consulta = consulta
        self.tarje_tade_credito = tarje_tade_credito
        self.Num_tarjeta = Num_tarjeta
        self.problema = problema
        self.estado_citas = estado_citas
    



with app.app_context():
    db.create_all()
