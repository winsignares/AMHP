from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from flask_sqlalchemy import SQLAlchemy
from model.cita import citas
from model.odontologo import odontologos
# from datetime import datetime,time

routes_cita_user = Blueprint("routes_cita_user", __name__)



@routes_cita_user.route('/guardarcitas', methods=['POST'])
def savecita():

    Nombre_completo = request.form['Nombre_completo'] 
    Edad = request.form['Edad']
    genero = request.form['genero']
    fecha = request.form['fecha']
    consulta = request.form['consulta']
    tarje_tade_credito = request.form['tarje_tade_credito']
    Num_tarjeta = request.form['Num_tarjeta']
    estado_cita = request.form['estado_cita']
    problema = request.form['problema']
    # problema = date.today()
    print(Nombre_completo)
    new_cit = citas( Nombre_completo, Edad,genero,fecha,consulta,tarje_tade_credito, Num_tarjeta,estado_cita,problema)
    db.session.add(new_cit)
    db.session.commit()
    return "si" 



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
