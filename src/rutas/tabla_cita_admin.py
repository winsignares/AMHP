from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.cita import citas
from model.paciente import pacientes
from model.odontologo import odontologos
from model.admin import admins
import secrets
from model.fechas_disponibles import fechas_disponi
import datetime
routes_cita_admin = Blueprint("routes_cita_admin", __name__)



@routes_cita_admin.route('/mostrar_citas_admin', methods=['GET'])
def mostarcitasuser():
    datos = {}
    admin_id = session.get("admin_id")  # Obtener el ID del administrador de la sesión
    admin_principal = db.session.query(admins).filter(admins.id == admin_id, admins.tipo_admin == 1).first()

    if admin_principal:  # Si el administrador actual es el administrador principal
        resultado = db.session.query(citas, pacientes, odontologos, fechas_disponi).select_from(citas).join(pacientes).join(odontologos).join(fechas_disponi).all()
    else:
        resultado = db.session.query(citas, pacientes, odontologos, fechas_disponi).select_from(citas).join(pacientes).join(odontologos).join(fechas_disponi).filter(citas.id_admin == admin_id).all()

    i = 0
    goria = []
    for cate, paciente, odontolo, fecha_dis in resultado:
        i += 1	       
        datos[i] = {
            'id': cate.id,
            'Rol': cate.Rol,
            'Codigo': cate.codigo_s	,
            'Nombre_completos': paciente.Name,
            'Cedula': paciente.cedula,                                                     
            'nombre_odontologos': odontolo.nombre,                                                    
            'fecha': fecha_dis.fechas_dispon,                                                    
            'consulta': cate.consulta,                                                    
            'tarje_credi': cate.tarje_tade_credito,                                                    
            'Num_tarjeta': cate.Num_tarjeta,                                                      
            'estado_citas': cate.estado_citas,                                                     
            'problema': cate.problema                                                     
        }
        goria.append(datos)
    return jsonify(datos)




# esto mustra los nombre de los pacientes el un select del formulario de agender cita como admin
@routes_cita_admin.route('/obtener_nombres_pacientes')
def obtener_nombres_pacientes():
    datos = []
    admin_id = session.get("admin_id")  # Obtener el ID del administrador actualmente logueado
    admin_principal = db.session.query(admins).filter(admins.id == admin_id, admins.tipo_admin == 1).first()

    if admin_principal:  # Si el administrador actual es el administrador principal
        subquery = db.session.query(citas.id_paciente).distinct()
        resultado = db.session.query(pacientes).filter(
            (~pacientes.id.in_(subquery))
        ).all()
    else:
        subquery = db.session.query(citas.id_paciente).distinct()
        resultado = db.session.query(pacientes).filter(
            (~pacientes.id.in_(subquery)) & (pacientes.id_admin == admin_id)
        ).all()

    for cate in resultado:
        datos.append({
            'id_paciente': cate.id,
            'Nombre_paciente': cate.Name
        })

    return jsonify(datos)



@routes_cita_admin.route('/guardarcitas_admin', methods=['POST'])
def savecita_admins():
    Rol = "admin"
    fecha = request.form['fecha']
    consulta = request.form['consulta']
    tarje_tade_credito = request.form['tarje_tade_credito']
    Num_tarjeta = request.form['Num_tarjeta']
    cita_estado = request.form['cita_estado']
    problema = request.form['problema']
    id_paciente = request.form['Nombre_completo']
    id_odontologo = request.form['odontlogos']
    id_admin = session.get("admin_id")
    codigo = secrets.token_hex(4) 
    
    new_cit = citas(codigo, Rol, consulta, tarje_tade_credito, Num_tarjeta, cita_estado, problema, id_paciente, id_odontologo, fecha, id_admin)
    db.session.add(new_cit)
    db.session.commit()
    
    return jsonify({"message": "Se guardó la cita exitosamente", "codigo": codigo})

    
#mustra los datos de fercha disponible en un select
@routes_cita_admin.route('/obtener_fechas_dispo')
def obtener_fechas_dispo_select():
    datos = []
    admin_id = session.get("admin_id")  # Obtener el ID del administrador actualmente logueado
    admin_principal = db.session.query(admins).filter(admins.id == admin_id, admins.tipo_admin == 1).first()

    if admin_principal:  # Si el administrador actual es el administrador principal
        subquery = db.session.query(citas.id_fechadispo).distinct()
        resultado = db.session.query(fechas_disponi).filter(
            fechas_disponi.id.notin_(subquery)
        ).all()
    else:
        subquery = db.session.query(citas.id_fechadispo).distinct()
        resultado = db.session.query(fechas_disponi).filter(
            (fechas_disponi.id.notin_(subquery)) & (fechas_disponi.id_admin == admin_id)
        ).all()

    for cate in resultado:
        datos.append({
            'id_fechadisp': cate.id,
            'fecha_disp': cate.fechas_dispon
        })

    return jsonify(datos)



# esto es para eliminar citas como admin
@routes_cita_admin.route('/eliminar_citas_admin', methods=['POST'])
def eliminar_citas_admin():
    # Obtener el ID del odontologo a eliminar desde la solicitud POST
    id_citas = request.json['id']

    # Lógica para eliminar el odontologo en la base de datos
    # Aquí debes escribir el código para eliminar el odontologo utilizando la biblioteca o método que estés utilizando para interactuar con la base de datos
    
    cita = citas.query.get(id_citas)  # Busca el odontologo por ID
    if cita:
        db.session.delete(cita)  # Elimina el odontologo
        db.session.commit()  # Confirma los cambios en la base de datos
        return jsonify({'message': 'cita eliminado correctamente'})
    else:
        return jsonify({'message': 'cita no encontrado'})
    


# actualizar citas
@routes_cita_admin.route('/actualizar_citas_admin', methods=['POST'] )
def actualizar_cita_admin():
  
  # Obtener los datos enviados en la solicitud
    id = request.form.get('id')

    fecha = request.form['fecha']
    consulta = request.form['consulta']
    tarje_tade_credito = request.form['tarje_tade_credito']
    Num_tarjeta = request.form['Num_tarjeta']
    cita_estado = request.form['cita_estado']
    problema = request.form['problema']
    id_paciente = request.form['Nombre_actualizar']
    id_odontologos = request.form['odontlogos_actualizar']

    # Obtener el registro existente de la base de datos
    cita_actualizar = citas.query.get(id)

    # Verificar qué campos se deben actualizar
 
    
    if consulta:
        cita_actualizar.consulta = consulta
    if tarje_tade_credito:
        cita_actualizar.tarje_tade_credito = tarje_tade_credito
    if Num_tarjeta:
        cita_actualizar.Num_tarjeta = Num_tarjeta
    if cita_estado:
        cita_actualizar.estado_citas = cita_estado
    if problema:
        cita_actualizar.problema = problema
    if id_paciente:
        cita_actualizar.id_paciente = id_paciente
    if id_odontologos:
        cita_actualizar.id_odontologos = id_odontologos
    if fecha:
        cita_actualizar.id_fechadispo = fecha

    # Guardar los cambios en la base de datos
    db.session.commit()
    return "se actualizo cita"


    # fechadis_actualizar=db.session.query(fechas_disponi).filter(fechas_disponi.fechas_dispon == fecha).first()
    # if fechadis_actualizar:
    #     db.session.delete(fechadis_actualizar)  # Elimina el fecha
    #     db.session.commit()  # Confirma los cambios en la base de datos
    #     return jsonify({'message': 'fecha eliminado correctamente y cita agendada'})
    # else:
    #     return jsonify({'message': 'fecha no encontrado'})
    



