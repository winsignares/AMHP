from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.cita import citas

routes_cita = Blueprint("routes_cita", __name__)


@routes_cita.route("/indexcita" )
def indexcita():
    titulo= "Pagina cita"
    return render_template('/main/cita.html', titles=titulo)


@routes_cita.route('/guardarcita',methods=['POST'])
def saveinstitution():

    nombre_completos = request.form['nombre_completo']
    edad = request.form['edad']
    #genero = request.form['genero'] 
    #fecha = request.form['fecha'] 
    #consulta = request.form['consulta'] 
    #tarje_tade_credito = request.form['tarje_tade_credito'] 
    numero_de_tarjeta = request.form['numero_de_tarjeta'] 
    print(nombre_completos)
    new_cita = citas (nombre_completos, edad,numero_de_tarjeta)
    db.session.add(new_cita)
    db.session.commit()
    return "si"
    



