from config.db import db, app, ma 
from werkzeug.security import generate_password_hash


class admins(db.Model):
    __tablename__ = "tbladmin"

    id = db.Column(db.Integer, primary_key=True)
    tipo_admin = db.Column(db.String(50))
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    contraseña = db.Column(db.String(128))  # Aumentar la longitud del campo para almacenar el hash

    def __init__(self, tipo_admin, nombre, apellido, correo, contraseña):
        self.tipo_admin = tipo_admin
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contraseña = generate_password_hash(contraseña)  # Generar el hash de la contraseña
 

        
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


