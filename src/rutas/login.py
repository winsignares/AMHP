from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.admin import admins


routes_login = Blueprint("routes_login", __name__)




@routes_login.route("/login", methods=["POST"])
def validar_login():
    usuario = request.json["usuario"]
    contraseña = request.json["contraseña"]
    verificacion = db.session.query(admins).filter(admins.correo == usuario).first()

    if verificacion:
        admin_id = verificacion.id  # Obtener el id del administrador

        if verificacion.contraseña == contraseña:
            session["admin_id"] = admin_id  # Guardar el admin_id en la sesión
            
            return {"status": "Correcto", "message": "Inicio de sesión exitoso"}
        else:
            return {"status": "Error", "message": "Contraseña incorrecta"}
    else:
        return {"status": "Error", "message": "Correo incorrecto"}
    

    
    
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

@routes_login.route('/mostrar_admins', methods=['GET'])
def mostrar_admins():
    datos= {}
    resultado = db.session.query(admins).select_from(admins).all()
    i=0
    goria = []
    for cate in resultado:
        i+=1	       
        datos[i] = {
        'id':cate.id,
        'tipo_admin':cate.tipo_admin,
		'nombre':cate.nombre,
		'apellido':cate.apellido,                                                                                                      
		'correo':cate.correo,                                                                                                      
		'contraseña':cate.contraseña,                                                                                                      
        }
        goria.append(datos)
    return jsonify(datos)
