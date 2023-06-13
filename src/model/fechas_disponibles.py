from config.db import db, app, ma 

class fechas_disponi(db.Model):
    __tablename__ = "tblfechadisponible"

    
    id  = db.Column(db.Integer, primary_key=True)
    fechas_dispon = db.Column(db.String(50))
    id_admin = db.Column(db.Integer,db.ForeignKey('tbladmin.id'), nullable=True)


    def __init__(self, fechas_dispon,id_admin=None):
        self.fechas_dispon = fechas_dispon
        self.id_admin = id_admin
    
     
with app.app_context():
    db.create_all()
