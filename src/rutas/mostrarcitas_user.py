from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.cita import citas 
# from model.paciente import registros

routes_mos_user = Blueprint("routes_mos_user", __name__)


@routes_mos_user.route("/tablauser" )
def indexcita2():
    titulo= "Pagina tabla user"
    return render_template('/main/tabla_cita_user.html', titles=titulo)


@routes_mos_user.route('/mostrar_citas_user', methods=['GET'] )
def actualizar_citas():

    datos= {}
    resultado = db.session.query(citas).select_from(citas).all()
    i=0
    goria = []
    for cate in resultado:
        i+=1	       
        datos[i] = {
        'id':cate.id,
		'Nombre_completo':cate.Nombre_completo,
		'Edad':cate.Edad,                                                    
		'genero':cate.genero,                                                    
		'fecha':cate.fecha,                                                    
		'consulta':cate.consulta,                                                    
        }
        goria.append(datos)
    return jsonify(datos)

