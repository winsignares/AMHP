from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from flask_sqlalchemy import SQLAlchemy
from model.cita import citas

routes_cita = Blueprint("routes_cita", __name__)


@routes_cita.route("/indexcita",  methods=['GET'])
def indexcita():
    titulo = "Pagina cita"
    return render_template('/main/savecita_user.html', titles=titulo)


@routes_cita.route('/guardarcita', methods=['POST'])
def savecita():

    Nombre_completo = request.form['Nombre_completo']
    Edad = request.form['Edad']
    genero = request.form['genero']
    fecha = request.form['fecha']
    consulta = request.form['consulta']
    tarje_tade_credito = request.form['tarje_tade_credito']
    Num_tarjeta = request.form['Num_tarjeta']
    problema = request.form['problema']
    print(Nombre_completo)
    new_cit = citas( Nombre_completo, Edad,genero,fecha,consulta,tarje_tade_credito, Num_tarjeta,problema)
    db.session.add(new_cit)
    db.session.commit()
    return "si"
