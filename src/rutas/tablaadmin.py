from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.cita import citas
from model.paciente import pacientes
from model.fechas_disponibles import fechas_disponi

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
		'Nombre_completos':cate.Nombre_completo,
		'Edad':cate.Edad,                                                    
		'nombre_odontologos':cate.nombre_odontologo,                                                    
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
            
            'Nombre_paciente': cate.Name
        })
    return jsonify(datos)

@routes_cita2.route('/guardarcitas_admin', methods=['POST'])
def savecita_admins():

    Nombre_completo = request.form['Nombre_completo']
    Edad = request.form['Edad']
    genero = request.form['odontlogos']
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
 
#esto hace que se elimine el dato en la tabla fecha disponible apenas el usuario o admin elije esa fecha asi no se repiten las fechas 
    fechadis=db.session.query(fechas_disponi).filter(fechas_disponi.fechas_dispon == fecha).first()
    if fechadis:
        db.session.delete(fechadis)  # Elimina el fecha
        db.session.commit()  # Confirma los cambios en la base de datos
        return jsonify({'message': 'fecha eliminado correctamente y cita agendada'})
    else:
        return jsonify({'message': 'fecha no encontrado'})
    

 


# @routes_cita2.route('/updatesolicitudes', methods=['POST'] )
# def actualizarS():
#     id = request.json['id']
#     solicitudes = request.json['Nombre_proveedor','Telefono','Direccion','Descripcion']
#     pusuario = solicitudes.query.get(id)
#     pusuario.cantidad = solicitudes
#     db.session.commit()
#     return redirect('/updatesolicitudes')



#esta guada  la fecha disponible de la tabla fecha disponible
@routes_cita2.route('ingresar_fechas_disponibles', methods=['POST'])
def fecha_dis():
    fechas_dispon = request.form['fechas_dispon']
    new_fecha = fechas_disponi(fechas_dispon)
    db.session.add(new_fecha)
    db.session.commit()
    return "si se puso la fecha disponoble"

#mustra los datos de fercha disponible en un select
@routes_cita2.route('/obtener_fechas_dispo')
def obtener_fechas_dispo():
    datos = []
    resultado = db.session.query(fechas_disponi).select_from(fechas_disponi).all()
    i = 0
    for cate in resultado:
        i += 1	       
        datos.append({
            'fecha_disp': cate.fechas_dispon
        })
    return jsonify(datos)


# esto es para eliminar citas como admin
@routes_cita2.route('/eliminar_citas_admin', methods=['POST'])
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
@routes_cita2.route('/actualizar_citas_admin', methods=['POST'] )
def actualizar_cita_admin():
  # Obtener los datos enviados en la solicitud
    id = request.form.get('id')
    Nombre_completo = request.form['Nombre_completo']
    Edad = request.form['Edad']
    nombre_odontologo = request.form['odontlogos']
    fecha = request.form['fecha']
    consulta = request.form['consulta']
    tarje_tade_credito = request.form['tarje_tade_credito']
    Num_tarjeta = request.form['Num_tarjeta']
    cita_estado = request.form['cita_estado']
    problema = request.form['problema']

    # Aquí puedes realizar las operaciones necesarias para actualizar los datos en la base de datos
    # por ejemplo, usando un ORM como SQLAlchemy o ejecutando consultas directas a la base de datos

    # Ejemplo de actualización usando SQLAlchemy
    cita_actualizar = citas.query.get(id)
    cita_actualizar.Nombre_completo = Nombre_completo
    cita_actualizar.Edad = Edad
    cita_actualizar.nombre_odontologo = nombre_odontologo
    cita_actualizar.fecha = fecha
    cita_actualizar.consulta = consulta
    cita_actualizar.tarje_tade_credito = tarje_tade_credito
    cita_actualizar.Num_tarjeta = Num_tarjeta
    cita_actualizar.estado_citas = cita_estado
    cita_actualizar.problema = problema

    # Guardar los cambios en la base de datos
    db.session.commit()
      
    # Enviar una respuesta exitosa
    return jsonify({'message': 'Datos actualizados correctamente de la cita'})


