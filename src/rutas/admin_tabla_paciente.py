from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.registro import registros

routes_admin_tabla_paciente = Blueprint("routes_admin_tabla_paciente", __name__)


@routes_admin_tabla_paciente.route("/indexadmin_tabla_paciente" )
def indexadmin_tabla_paciente():
    titulo= "Pagina admin_tabla_paciente"
    return render_template('/main/admin_tabla_paciente.html', titles=titulo)


@routes_admin_tabla_paciente.route('/guardarpaciente_admin', methods=['POST'])
def saveregistro_admin():
    Names = request.form['Name']
    cedulas = request.form['cedula']
    telefonos = request.form['telefono']
    direccions = request.form['direccion']
    Emails = request.form['Email']
    fecha_nacimientos = request.form['fecha_nacimiento']
    print(Names)
    new_reg = registros(Names,cedulas,telefonos,direccions,Emails,fecha_nacimientos)
    db.session.add(new_reg)
    db.session.commit()
    return "si"

@routes_admin_tabla_paciente.route('/mostrar_pacientes_admin', methods=['GET'])
def mostarpaciente_admin():
    datos= {}
    resultado = db.session.query(registros).select_from(registros).all()
    i=0
    goria = []
    for cate in resultado:
        i+=1	       
        datos[i] = {
        'id':cate.id,
		'Name':cate.Name,
		'cedula':cate.cedula,                                                    
		'telefono':cate.telefono,                                                    
		'direccion':cate.direccion,                                                    
		'Email':cate.Email,                                                    
		'fecha_nacimiento':cate.fecha_nacimiento,                                                    
        }
        goria.append(datos)
    return jsonify(datos)
