from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.cita import citas
from model.paciente import pacientes

routes_cita2 = Blueprint("routes_cita2", __name__)



@routes_cita2.route('/mostrar_citas_admin', methods=['GET'])
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
		'tarje_credi':cate.tarje_tade_credito,                                                    
		'Num_tarjeta':cate.Num_tarjeta,                                                    
		'estado_citas':cate.estado_citas,                                                    
		'problema':cate.problema                                                     
        }
        goria.append(datos)
    return jsonify(datos)

@routes_cita2.route('/obtener_nombres_pacientes')
def obtener_nombres_pacientes():
    datos = []
    resultado = db.session.query(pacientes).select_from(pacientes).all()
    i = 0
    for cate in resultado:
        i += 1	       
        datos.append({
            
            'Nombre_completo': cate.Name
        })
    return jsonify(datos)

@routes_cita2.route('/guardarcitas_admin', methods=['POST'])
def savecita_admins():

    Nombre_completo = request.form['Nombre_completo']
    Edad = request.form['Edad']
    genero = request.form['genero']
    fecha = request.form['fecha']
    consulta = request.form['consulta']
    tarje_tade_credito = request.form['tarje_tade_credito']
    Num_tarjeta = request.form['Num_tarjeta']
    cita_estado = request.form['cita_estado']
    problema = request.form['problema']
    # problema = date.today()
    print(Nombre_completo)
    new_cit = citas( Nombre_completo, Edad,genero,fecha,consulta,tarje_tade_credito, Num_tarjeta,cita_estado,problema)
    db.session.add(new_cit)
    db.session.commit()
    return "si" 


# @routes_cita2.route('/updatesolicitudes', methods=['POST'] )
# def actualizarS():
#     id = request.json['id']
#     solicitudes = request.json['Nombre_proveedor','Telefono','Direccion','Descripcion']
#     pusuario = solicitudes.query.get(id)
#     pusuario.cantidad = solicitudes
#     db.session.commit()
#     return redirect('/updatesolicitudes')


