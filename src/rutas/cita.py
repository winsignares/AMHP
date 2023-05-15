from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from flask_sqlalchemy import SQLAlchemy
from model.cita import citas
# from datetime import datetime,time

routes_cita = Blueprint("routes_cita", __name__)



@routes_cita.route('/guardarcitas', methods=['POST'])
def savecita():

    Nombre_completo = request.form['Nombre_completo']
    Edad = request.form['Edad']
    genero = request.form['genero']
    fecha = request.form['fecha']
    consulta = request.form['consulta']
    tarje_tade_credito = request.form['tarje_tade_credito']
    Num_tarjeta = request.form['Num_tarjeta']
    problema = request.form['problema']
    id_paciente = request.form['id_paciente']
    id_odontologos = request.form['id_odontologos']
    # problema = date.today()
    print(Nombre_completo)
    new_cit = citas( Nombre_completo, Edad,genero,fecha,consulta,tarje_tade_credito, Num_tarjeta,problema,id_paciente,id_odontologos)
    db.session.add(new_cit)
    db.session.commit()
    return "si" 
