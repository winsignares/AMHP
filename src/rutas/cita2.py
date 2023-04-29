from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.cita import citas

routes_cita2 = Blueprint("routes_cita2", __name__)


@routes_cita2.route("/indexcita2" )
def indexcita2():
    titulo= "Pagina cita2"
    return render_template('/main/cita2.html', titles=titulo)



@routes_cita2.route('/mostrar_citas_user', methods=['GET'])
def mostarcitasuser():
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


@routes_cita2.route('/actualizar_citas', methods=['POST'] )
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


@routes_cita2.route('/updatesolicitudes', methods=['POST'] )
def actualizarS():
    id = request.json['id']
    solicitudes = request.json['Nombre_proveedor','Telefono','Direccion','Descripcion']
    pusuario = Solicitudes.query.get(id)
    pusuario.cantidad = solicitudes
    db.session.commit()
    return redirect('/updatesolicitudes')


