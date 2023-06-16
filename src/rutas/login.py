from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.admin import admins
from werkzeug.security import generate_password_hash , check_password_hash
from model.cita import citas
from model.fechas_disponibles import fechas_disponi
from model.paciente import pacientes
from model.odontologo import odontologos
routes_login = Blueprint("routes_login", __name__)




@routes_login.route('/login', methods=['POST'])
def validar_login():
    usuario = request.json["usuario"]
    contraseña = request.json["contraseña"]
    verificacion = db.session.query(admins).filter(admins.correo == usuario).first()

    if verificacion:
        admin_id = verificacion.id  # Obtener el ID del administrador
        admin_nombre = verificacion.nombre  # Obtener el nombre del administrador

        if check_password_hash(verificacion.contraseña, contraseña):
            session["admin_id"] = admin_id  # Guardar el admin_id en la sesión
            session["admin_nombre"] = admin_nombre  # Guardar el nombre del administrador en la sesión
           

            return {"status": "Correcto", "message": "Inicio de sesión exitoso"}
        else:
            return {"status": "Error", "message": "Contraseña incorrecta"}
    else:
        return {"status": "Error", "message": "Correo incorrecto"}
    
    
    
@routes_login.route('/guardar_admin', methods=['POST'])
def guardar_admins():
    admin_id = session.get("admin_id")  # Obtener el ID del administrador de la sesión
    admin_principal = db.session.query(admins).filter(admins.id == admin_id, admins.tipo_admin == 1).first()

    if admin_principal:  # Si el administrador actual es el administrador principal
        tipo_admin = 2
        name_admin = request.form['name_admin']
        apellido_admin = request.form['apellido_admin']
        correo_admin = request.form['correo_admin']
        contra_admin = request.form['contra_admin']

        # Check if the administrator already exists in the database 
        existing_admin = admins.query.filter_by(correo=correo_admin).first()
        if existing_admin:
            return "El administrador ya existe en la base de datos"

        new_admin = admins(tipo_admin, name_admin, apellido_admin, correo_admin, contra_admin)
        db.session.add(new_admin)
        db.session.commit()
        return "Registro exitoso" 
    else:
        return "No tienes permiso para realizar esta acción"


@routes_login.route('/mostrar_admins', methods=['GET'])
def mostrar_admins():
    admin_id = session.get("admin_id")  # Obtener el ID del administrador de la sesión
    admin_principal = db.session.query(admins).filter(admins.id == admin_id, admins.tipo_admin == 1).first()

    if admin_principal:  # Si el administrador actual es el administrador principal 
        datos = {}
        resultado = db.session.query(admins).select_from(admins).all()
        i = 0
        for cate in resultado:
            i += 1
            datos[i] = {
                'id': cate.id,
                'tipo_admin': cate.tipo_admin,
                'nombre': cate.nombre,
                'apellido': cate.apellido,
                'correo': cate.correo,
                'contraseña': cate.contraseña,
            }
        return jsonify(datos)
    else:
        return "No tienes permiso para realizar esta acción"


 

# esto es para eliminar citas como admin
@routes_login.route('/elimina_admin', methods=['POST'])
def elimina_admin():
    # Obtener el ID del admin a eliminar desde la solicitud POST
    id_admin = request.json['id']

    # Lógica para eliminar el admin en la base de datos
    # Aquí debes escribir el código para eliminar el admin utilizando la biblioteca o método que estés utilizando para interactuar con la base de datos
    # esta pequeña validacion es por si el admin tiene aolgunas de estas asociadas esta le manda una alerta diciendo que no se puede eliminar
    admin_principal = admins.query.filter_by(id=id_admin, tipo_admin=1).first()
    if admin_principal:
        return jsonify({'message': 'No se puede eliminar al administrador principal'})
        
    citas_admin = citas.query.filter_by(id_admin=id_admin).first()
    if citas_admin:
        return jsonify({'message': 'No se puede eliminar al admin porque tiene citas asociadas'})
    

    fechadispo_admin = fechas_disponi.query.filter_by(id_admin=id_admin).first()
    if fechadispo_admin:
        return jsonify({'message': 'No se puede eliminar al admin porque tiene fecha_dispo asociadas'})
    
    pacientes_admin = pacientes.query.filter_by(id_admin=id_admin).first()
    if pacientes_admin:
        return jsonify({'message': 'No se puede eliminar al admin porque tiene paciente asociadas'})
    
    odontologo_admin = odontologos.query.filter_by(id_admin=id_admin).first()
    if odontologo_admin:
        return jsonify({'message': 'No se puede eliminar al admin porque tiene odontologo asociadas'})
    

    # aqui ya estaria eliminando al admin
    admin = admins.query.get(id_admin)  # Busca el odontologo por ID
    if admin:
        db.session.delete(admin)  # Elimina el odontologo
        db.session.commit()  # Confirma los cambios en la base de datos
        return jsonify({'message': 'admin eliminado correctamente'})
    else:
        return jsonify({'message': 'admin no encontrado'})
    

# actualizar admin
@routes_login.route('/actualizar_admin', methods=['POST'] )
def actualizar_admin():
  
  # Obtener los datos enviados en la solicitud
    id = request.form.get('id')

    nombre_admin_nuevo = request.form['nombre_admin_nuevo']
    apellido_admin_nuevo = request.form['apellido_admin_nuevo']
    correo_admin = request.form['correo_admin']
    conrasena_admin_nuevo = request.form['conrasena_admin_nuevo']

    # Obtener el registro existente de la base de datos
    admin_actualizar = admins.query.get(id)

    # Verificar qué campos se deben actualizar

    if nombre_admin_nuevo:
        admin_existente = admins.query.filter_by(nombre=nombre_admin_nuevo).first()
        if admin_existente:
            return jsonify({'message': 'El nombre ya existe en otro administrador'})
        admin_actualizar.nombre = nombre_admin_nuevo
    if apellido_admin_nuevo:
        # Verificar si el nuevo apellido ya existe en otro registro
        admin_existente = admins.query.filter_by(apellido=apellido_admin_nuevo).first()
        if admin_existente:
            return jsonify({'message': 'El apellido ya existe en otro administrador'})
        admin_actualizar.apellido = apellido_admin_nuevo
    
    if correo_admin:
        # Verificar si el nuevo correo ya existe en otro registro
        admin_existente = admins.query.filter_by(correo=correo_admin).first()
        if admin_existente:
            return jsonify({'message': 'El correo ya existe en otro administrador'})
        admin_actualizar.correo = correo_admin
        
    if conrasena_admin_nuevo:
        # Encriptar la nueva contraseña
        hashed_password = generate_password_hash(conrasena_admin_nuevo)
        admin_actualizar.contraseña = hashed_password

    # Guardar los cambios en la base de datos
    db.session.commit()
    return "se actualizo admin"
