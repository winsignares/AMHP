from config.db import db, app, ma 

class registro(db.Model):
    __tablename__ = "tblregistro"

    
    id  = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50))
    Username = db.Column(db.String(50))
    Email = db.Column(db.String(50))
    Password = db.Column(db.String(50))

    def __init__(self, Name,Username,Email,Password):
        self.Name = Name
        self.Username = Username
        self.Email = Email
        self.Password = Password
     
with app.app_context():
    db.create_all()
