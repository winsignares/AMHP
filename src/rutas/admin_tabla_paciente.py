from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.paciente import pacientes
from model.cita import citas
from datetime import datetime,date
routes_admin_tabla_paciente = Blueprint("routes_admin_tabla_paciente", __name__)



@routes_admin_tabla_paciente.route('/guardarpaciente_admin', methods=['POST']) 
def saveregistro_admin():
    Rol = "admin"
    fecha_registro = date.today()
    Name = request.form['Name']
    edad = request.form['edad']
    cedula = request.form['cedula']
    telefono = request.form['telefono']
    direccion = request.form['direccion']
    Email = request.form['Email']
    fecha_nacimiento = request.form['fecha_nacimiento']

    # Check if the patient already exists in the database
    existing_patient = pacientes.query.filter(
        (pacientes.cedula == cedula) | (pacientes.Email == Email)
    ).first()
    if existing_patient:
        return "Paciente already exists in the database"

    new_reg = pacientes(Rol,fecha_registro,Name,edad, cedula, telefono, direccion, Email, fecha_nacimiento)
    db.session.add(new_reg)
    db.session.commit()
    return "Record saved successfully"


@routes_admin_tabla_paciente.route('/eliminar_paciente_admin', methods=['POST'])
def eliminar_paciente_admin():
    # Obtener el ID del paciente a eliminar desde la solicitud POST
    id_paciente = request.json['id']

    # Verificar si el paciente tiene citas asociadas
    citas_paciente = citas.query.filter_by(id_paciente=id_paciente).first()
    if citas_paciente:
        return jsonify({'message': 'No se puede eliminar al paciente porque tiene citas asociadas'})

    # Lógica para eliminar el paciente en la base de datos
    paciente = pacientes.query.get(id_paciente)  # Busca el paciente por ID
    if paciente:
        db.session.delete(paciente)  # Elimina el paciente
        db.session.commit()  # Confirma los cambios en la base de datos
        return jsonify({'message': 'Paciente eliminado correctamente'})
    else:
        return jsonify({'message': 'Paciente no encontrado'})
    
@routes_admin_tabla_paciente.route('/mostrar_pacientes_admin', methods=['GET'])
def mostarpaciente_admin():
    datos= {}
    resultado = db.session.query(pacientes).select_from(pacientes).all()
    i=0
    goria = []
    for cate in resultado:
        i+=1	       
        datos[i] = { 
        'id':cate.id,
		'Rol':cate.Rol,
		'fecha_de_regitro':cate.fecha_de_regitro,
		'Name':cate.Name,
		'edad':cate.edad,
		'cedula':cate.cedula,                                                    
		'telefono':cate.telefono,                                                    
		'direccion':cate.direccion,                                                    
		'Email':cate.Email,                                                    
		'fecha_nacimiento':cate.fecha_nacimiento,                                                    
        }
        goria.append(datos)
    return jsonify(datos)


@routes_admin_tabla_paciente.route('/actualizar_paciente_admin', methods=['POST'])
def actualizar_paciente():
    # Obtener los datos enviados en la solicitud
    id = request.form.get('id')
    name = request.form.get('Name')
    edad = request.form.get('edad_new')
    cedula = request.form.get('cedula')
    telefono = request.form.get('telefono')
    direccion = request.form.get('direccion')
    email = request.form.get('Email')
    fecha_nacimiento = request.form.get('fecha_nacimiento')

    # Obtener el registro existente de la base de datos
    paciente = pacientes.query.get(id)

    # Verificar qué campos se deben actualizar
    if name:
        paciente.Name = name
    if edad:
        paciente.edad = edad
    if cedula:
        paciente.cedula = cedula
    if telefono:
        paciente.telefono = telefono
    if direccion:
        paciente.direccion = direccion
    if email:
        paciente.Email = email
    if fecha_nacimiento:
        paciente.fecha_nacimiento = fecha_nacimiento

    # Guardar los cambios en la base de datos
    db.session.commit()

    # Enviar una respuesta exitosa
    return jsonify({'message': 'Datos actualizados correctamente'})

