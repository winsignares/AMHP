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

    def __init__(self, Nombre_completo, Edad,genero,fecha,consulta,tarje_tade_credito, Num_tarjeta):
        self.Nombre_completo = Nombre_completo
        self.Edad = Edad
        self.genero = genero
        self.fecha = fecha
        self.consulta = consulta
        self.tarje_tade_credito = tarje_tade_credito
        self.Num_tarjeta = Num_tarjeta


with app.app_context():
    db.create_all()
