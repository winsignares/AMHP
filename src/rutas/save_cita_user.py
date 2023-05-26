from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from flask_sqlalchemy import SQLAlchemy
from model.cita import citas
from model.odontologo import odontologos 
from model.fechas_disponibles import fechas_disponi 
# from datetime import datetime,time

routes_cita_user = Blueprint("routes_cita_user", __name__)



@routes_cita_user.route('/guardarcitas', methods=['POST'])
def savecita():

    Nombre_completo = request.form['Nombre_completo'] 
    Edad = request.form['Edad']
    genero = request.form['genero']
    fechadi = request.form['fecha']
    consulta = request.form['consulta']
    tarje_tade_credito = request.form['tarje_tade_credito']
    Num_tarjeta = request.form['Num_tarjeta']
    estado_cita = request.form['estado_cita']
    problema = request.form['problema']
    # problema = date.today()
    print(Nombre_completo)
    new_cit = citas( Nombre_completo, Edad,genero,fechadi,consulta,tarje_tade_credito, Num_tarjeta,estado_cita,problema)
    db.session.add(new_cit)
    db.session.commit()

#esto hace que se elimine el dato en la tabla fecha disponible apenas el usuario o admin elije esa fecha asi no se repiten las fechas 
    fechas_disponibles=db.session.query(fechas_disponi).filter(fechas_disponi.fechas_dispon == fechadi).first()
    if fechas_disponibles:
        db.session.delete(fechas_disponibles)  # Elimina el fecha
        db.session.commit()  # Confirma los cambios en la base de datos
        return jsonify({'message': 'fecha eliminado correctamente y cita agendada como user'})
    else:
        return jsonify({'message': 'fecha no encontrado como user'})
    



#este codigo saca solo el dato del nombre del odontologo para mostrarlo en un select
@routes_cita_user.route('/select_odontologo_mostrars')
def select_odontologo_mostrar():
    datos = []
    resultado = db.session.query(odontologos).select_from(odontologos).all()
    i = 0
    for odon in resultado:
        i += 1	       
        datos.append({
            
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

