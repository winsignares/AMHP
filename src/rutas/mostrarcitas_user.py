from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.cita import citas 
# from model.paciente import registros

routes_mos_user = Blueprint("routes_mos_user", __name__)



@routes_mos_user.route("/buscarcita_user", methods=["POST"])
def buscar_cita():
  
    id_buscar = request.json["buscar"]
    datos= {}
    resultado = db.session.query(citas).filter(citas.id == id_buscar).all()

    i=0
    goria = []
    for cate in resultado:
        i+=1	       
        datos[i] = {
        'id':cate.id,
		'Nombre_completos':cate.Nombre_completo,
		'Edad':cate.Edad,                                                    
		'nombre_odontologos':cate.nombre_odontologo,                                                    
		'fecha':cate.fecha,                                                    
		'consulta':cate.consulta,                                                    
		# 'tarje_credi':cate.tarje_tade_credito,                                                    
		# 'Num_tarjeta':cate.Num_tarjeta,                                                    
		'estado_citas':cate.estado_citas,                                                    
		'problema':cate.problema                                                      
        }
        goria.append(datos) 
    return jsonify(datos)
  

    