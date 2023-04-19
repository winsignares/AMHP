from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.paciente import pacientes

routes_cita = Blueprint("routes_cita", __name__)


@routes_cita.route("/indexcita" )
def indexcita():
    titulo= "Pagina cita"
    return render_template('/main/cita.html', titles=titulo)


@routes_cita.route('/guardarinstitution',methods=['POST'])
def saveinstitution():

    codigo_infraestructura = request.form['codigo_infraestructura']
    nombre_institucion = request.form['nombre_institucion']
    distrito = request.form['distrito'] 
    telefono = request.form['telefono'] 
    año = request.form['año'] 
    print(codigo_infraestructura)
    new_institution = pacientes(codigo_infraestructura, nombre_institucion, distrito,telefono,año)
    db.session.add(new_institution)
    db.session.commit()
    return render_template('/main/institution.html')



