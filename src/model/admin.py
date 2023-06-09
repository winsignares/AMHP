from config.db import db, app, ma 

class admins(db.Model):
    __tablename__ = "tbladmin"

    
    id  = db.Column(db.Integer, primary_key=True)
    tipo_admin  = db.Column(db.String(50))
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    contraseña = db.Column(db.String(50))
    # tipo_user = db.Column(db.Integer)
    # id_citas= db.Column(db.Integer,db.ForeignKey('tblcitas.id'))

    def __init__(self,tipo_admin,nombre,apellido, correo,contraseña):
        self.tipo_admin = tipo_admin
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contraseña = contraseña
        # self.tipo_user = tipo_use
        
def create_admins():
    # Verificar si ya existen registros en la tabla
    if admins.query.count() == 0:
        # Crear registros de administradores
        admin1 = admins("1", "edwin", "escorcia", "1", "1")
    

        # Guardar los registros en la base de datos
        db.session.add(admin1)
        
        db.session.commit()

with app.app_context():
    db.create_all()
    create_admins()


