from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
# from model.paciente import pacientes
from model.odontologo import odontologos

routes_admin_tabla_medico = Blueprint("routes_admin_tabla_medico", __name__)


@routes_admin_tabla_medico.route("/indexadmin_tabla_medico" )
def indexadmin_tabla_medico():
    titulo= "Pagina admin_tabla_medico"
    return render_template('/main/admin_tabla_medico.html', titles=titulo)


@routes_admin_tabla_medico.route('/guardarodontologos_admin', methods=['POST'])
def saveodontologos_admin():
    nombre = request.form['nombre']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    correo = request.form['correo']
    especialidad = request.form['especialidad']     
    print(nombre)
    new_reg = odontologos(nombre,direccion,telefono,correo,especialidad)
    db.session.add(new_reg)
    db.session.commit()
    return "si"


@routes_admin_tabla_medico.route('/mostrar_odontologos_admin', methods=['GET'])
def mostarodontologo_admin():
    datos= {}
    resultado = db.session.query(odontologos).select_from(odontologos).all()
    i=0
    goria = []
    for cate in resultado:
        i+=1	       
        datos[i] = {
        'id':cate.id,
		'nombre':cate.nombre,
		'direccion':cate.direccion,                                                    
		'telefono':cate.telefono,                                                    
		'correo':cate.correo,                                                                                                       
		'especialidad':cate.especialidad,                                                                                                       
        }
        goria.append(datos)
    return jsonify(datos)
