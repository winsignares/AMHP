from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.cita import citas 
from model.paciente    import pacientes	
from model.odontologo    import odontologos	
from model.fechas_disponibles    import fechas_disponi	

# from model.paciente import registros

routes_mos_user = Blueprint("routes_mos_user", __name__)



# @routes_mos_user.route('/der', methods=['GET'])
# def mostarcitasuser():
    
#     datos= {}
#     resultado = db.session.query(citas,pacientes,odontologos).select_from(citas).join(pacientes).join(odontologos).all()
#     # filter(admins.id == admin_id, admins.tipo_admin == 1).first()
#     i=0
#     goria = []
#     for cita,paciente,odontolo in resultado:
#         i+=1	       
#         datos[i] = {
#          'id': cita.id,
#          'codigo_cita': cita.codigo_s,
#             'Nombre_completos': paciente.Name,
#             'nombre_odontologos': odontolo.nombre,
#             'consulta': cita.consulta,
#             'estado_citas': cita.estado_citas,
#             'problema': cita.problema                                                  
#         }
#         goria.append(datos)
#     return jsonify(datos)
 
@routes_mos_user.route("/der", methods=["POST"])
def mostarcitasuser():
    cedula_buscar = request.json["codigo_cita_buscar"]
    datos = {}
    
    resultado = db.session.query(citas, pacientes, odontologos,fechas_disponi).select_from(citas).join(pacientes).join(odontologos).join(fechas_disponi).filter(citas.codigo_s == cedula_buscar).all()
    i = 0
    goria = []
    for cita,paciente,odontolo,fechas_disponis in resultado:
        i += 1
        datos[i] = {
        'id': cita.id,
         'codigo_cita': cita.codigo_s,
         'fechas_disponissss': fechas_disponis.fechas_dispon,
            'Nombre_completos': paciente.Name,
            'nombre_odontologos': odontolo.nombre,
            'consulta': cita.consulta,
            'estado_citas': cita.estado_citas,
            'problema': cita.problema     
        }
        goria.append(datos)
    return jsonify(datos)