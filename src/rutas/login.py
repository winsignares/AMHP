from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.admin import admins


routes_login = Blueprint("routes_login", __name__)


@routes_login.route("/login", methods=["POST"])
def validar_login():
    usuario = request.json["usuario"]
    contraseña = request.json["contraseña"]
    verificacion = db.session.query(admins).filter(admins.correo == usuario,admins.contraseña == contraseña).first()

    # Busca el usuario en la base de datos
    if verificacion:
        return {"status": "Correcto", "message": "Inicio de sesión exitoso"}
    else:
        return {"status": "Error", "message": "Datos incorrectos"}

    
    
@routes_login.route('/guardar_admin', methods=['POST'])
def guardar_admins():
    tipo_admin = 2
    name_admin = request.form['name_admin']
    apellido_admin = request.form['apellido_admin']
    correo_admin = request.form['correo_admin']
    contra_admin = request.form['contra_admin']

    # Check if the administrator already exists in the database
    existing_admin = admins.query.filter_by(correo=correo_admin).first()
    if existing_admin:
        return "El administrador ya existe en la base de datos"

    new_admin = admins(tipo_admin,name_admin, apellido_admin, correo_admin, contra_admin)
    db.session.add(new_admin)
    db.session.commit()
    return "Registro exitoso"
