from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from flask_sqlalchemy import SQLAlchemy
from model.cita import citas
from model.odontologo import odontologos 
from model.paciente import pacientes 
from model.fechas_disponibles import fechas_disponi 
# from datetime import datetime,time

routes_cita_user = Blueprint("routes_cita_user", __name__)



@routes_cita_user.route('/guardarcitas_user', methods=['POST'])
def savecita_user():
    # Obtener los datos de la solicitud
    cedula = request.form['cedula_buscar']
    fecha = request.form['fecha']
    consulta = request.form['consulta']
    tarje_tade_credito = request.form['tarje_tade_credito']
    Num_tarjeta = request.form['Num_tarjeta']
    cita_estado = request.form['estado_cita']
    problema = request.form['problema']
    id_odontologo = request.form['odontlogos']
    fechadis = db.session.query(fechas_disponi).filter(fechas_disponi.fechas_dispon == fecha).first()
    # Verificar si la cédula existe en la base de datos
    # paciente = pacientes.query.filter_by(cedula=cedula).first()
    paciente = pacientes.query.filter( (pacientes.cedula == cedula) 
    ).first()
    if paciente:
        # Obtener el ID del paciente
        id_pacientes = paciente.id

        # Crear la nueva cita
        new_cit = citas(Rol="user", fecha=fecha, consulta=consulta, tarje_tade_credito=tarje_tade_credito,
                        Num_tarjeta=Num_tarjeta, estado_citas=cita_estado, problema=problema,
                        id_paciente=id_pacientes, id_odontologos=id_odontologo)

        db.session.add(new_cit)
        db.session.commit()
        
        # Eliminar la fecha disponible seleccionada
        
        if fechadis:
            db.session.delete(fechadis)
            db.session.commit()
      
        return"sisi"
    else:
       return "Paciente already exists in the database"




#este codigo saca solo el dato del nombre del odontologo para mostrarlo en un select
@routes_cita_user.route('/select_odontologo_mostrars')
def select_odontologo_mostrar():
    datos = []
    resultado = db.session.query(odontologos).select_from(odontologos).all()
    i = 0
    for odon in resultado:
        i += 1	       
        datos.append({
            
            'id_odontologo': odon.id, 
            'name_odontologo': odon.nombre 
        })
    return jsonify(datos)




#aqui se otiene las fechas dipoibles como user 
@routes_cita_user.route('/obtener_fechas_dispo_como_user')
def obtener_fechas_dispo():
    datos = []
    resultado = db.session.query(fechas_disponi).select_from(fechas_disponi).all()
    i = 0
    for cate in resultado:
        i += 1	       
        datos.append({
            'fecha_disponomble_user': cate.fechas_dispon
        })
    return jsonify(datos)

