from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
# from model.odontologos import odontologoss
from datetime import datetime,date
from model.odontologo import odontologos
from model.cita import citas
from model.admin import admins


routes_admin_tabla_medico = Blueprint("routes_admin_tabla_medico", __name__)




@routes_admin_tabla_medico.route('/guardarodontologos_admin', methods=['POST'])
def saveodontologos_admin():
    Rol = "Admin"
    fecha_registro = date.today()
    nombre = request.form['nombre']
    cedula = request.form['cedula_odon']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    correo = request.form['correo']
    especialidad = request.form['especialidad']  
    id_admin = session.get("admin_id")   
    print(nombre)
    
    # Check if the odontólogo already exists in the database
    existing_odontologo = odontologos.query.filter_by(cedula=cedula).first()
    if existing_odontologo:
        return "El odontólogo ya existe en la base de datos"
    
    newodontologo = odontologos(Rol, fecha_registro, nombre, cedula, direccion, telefono, correo, especialidad,id_admin)
    db.session.add(newodontologo)
    db.session.commit()
    return "Registro exitoso"



@routes_admin_tabla_medico.route('/mostrar_odontologos_admin', methods=['GET'])
def mostarodontologo_admin():
    datos = {}
    admin_id = session.get("admin_id")  # Obtener el ID del administrador de la sesión
    admin_principal = db.session.query(admins).filter(admins.id == admin_id, admins.tipo_admin == 1).first()

    if admin_principal:  # Si el administrador actual es el administrador principal
        resultado = db.session.query(odontologos, admins).select_from(odontologos).join(admins).all()
    else:
        resultado = (
            db.session.query(odontologos, admins)
            .select_from(odontologos)
            .join(admins)
            .filter(admins.id == admin_id)
            .all()
        )

    i = 0
    goria = []
    for cate, admin in resultado:
        i += 1	       
        datos[i] = {
            'id': cate.id,
            'Rol': cate.Rol,
            'nombre_admin': admin.nombre,
            'fecha_de_regitro': cate.fecha_de_regitro,
            'nombre': cate.nombre,
            'cedula': cate.cedula,
            'direccion': cate.direccion,
            'telefono': cate.telefono,
            'correo': cate.correo,
            'especialidad': cate.especialidad,
        }
        goria.append(datos)
    return jsonify(datos)



@routes_admin_tabla_medico.route('/eliminar_odontologo_admin', methods=['POST'])
def eliminar_odontologo_admin():
    # Obtener el ID del odontologo a eliminar desde la solicitud POST
    id_odontologo = request.json['id']

    # Lógica para eliminar el odontologo en la base de datos
    odontologo = odontologos.query.get(id_odontologo)  # Buscar el odontologo por ID
    if odontologo:
        # Verificar si hay citas asociadas al odontologo
        citas_odontologo = citas.query.filter_by(id_odontologos=id_odontologo).first()
        if citas_odontologo:
            return jsonify({'message': 'No se puede eliminar el odontologo porque tiene citas asociadas'})

        db.session.delete(odontologo)  # Eliminar el odontologo
        db.session.commit()  # Confirmar los cambios en la base de datos
        return jsonify({'message': 'odontologo eliminado correctamente'})
    else:
        return jsonify({'message': 'odontologo no encontrado'})
    



@routes_admin_tabla_medico.route('/actualizar_odontologos_admin', methods=['POST'])
def actualizar_odontologos():
    # Obtener los datos enviados en la solicitud
    id = request.form.get('id')
    nombre = request.form['nombre']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    correo = request.form['correo']
    especialidad = request.form['especialidad']

    # Obtener el registro existente de la base de datos
    odontologo = odontologos.query.get(id)

    # Verificar qué campos se deben actualizar
    if nombre:
        odontologo.nombre = nombre
    if direccion: 
        odontologo.direccion = direccion
    if telefono:
        odontologo.telefono = telefono
    if correo:
        odontologo.correo = correo
    if especialidad:
        odontologo.especialidad = especialidad

    # Guardar los cambios en la base de datos
    db.session.commit()

    # Enviar una respuesta exitosa
    return jsonify({'message': 'Datos actualizados correctamente'})



# esto hace que se muestre el monbre del odontologo en un select en el formulario de citas como admin
@routes_admin_tabla_medico.route('/obtener_nombres_odonlogo')
def obtener_nombres_odontologos():
    datos = []
    admin_id = session.get("admin_id")  # Obtener el ID del administrador actualmente logueado
    admin_principal = db.session.query(admins).filter(admins.id == admin_id, admins.tipo_admin == 1).first()

    if admin_principal:  # Si el administrador actual es el administrador principal
        subquery = db.session.query(citas.id_odontologos).distinct()
        resultado = db.session.query(odontologos).filter(
            (~odontologos.id.in_(subquery))
        ).all()
    else:
        subquery = db.session.query(citas.id_odontologos).distinct()
        resultado = db.session.query(odontologos).filter(
            (~odontologos.id.in_(subquery)) & (odontologos.id_admin == admin_id)
        ).all()

    for odon in resultado:
        datos.append({
            'id_odontologo': odon.id,
            'Nombre_odontologo': odon.nombre
        })

    return jsonify(datos)
