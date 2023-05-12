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
    newodontologo = odontologos(nombre,direccion,telefono,correo,especialidad)
    db.session.add(newodontologo)
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


@routes_admin_tabla_medico.route('/eliminar_odontologo_admin', methods=['POST'])
def eliminar_odontologo_admin():
    # Obtener el ID del odontologo a eliminar desde la solicitud POST
    id_odontologo = request.json['id']

    # Lógica para eliminar el odontologo en la base de datos
    # Aquí debes escribir el código para eliminar el odontologo utilizando la biblioteca o método que estés utilizando para interactuar con la base de datos
    
    odontologo = odontologos.query.get(id_odontologo)  # Busca el odontologo por ID
    if odontologo:
        db.session.delete(odontologo)  # Elimina el odontologo
        db.session.commit()  # Confirma los cambios en la base de datos
        return jsonify({'message': 'odontologo eliminado correctamente'})
    else:
        return jsonify({'message': 'odontologo no encontrado'})
    
    
@routes_admin_tabla_medico.route('/eliminar_paciente_admin', methods=['POST'])
def eliminar_paciente_admin():
    # Obtener el ID del paciente a eliminar desde la solicitud POST
    id_paciente = request.json['id']

    # Lógica para eliminar el paciente en la base de datos
    # Aquí debes escribir el código para eliminar el paciente utilizando la biblioteca o método que estés utilizando para interactuar con la base de datos
    
    paciente = odontologos.query.get(id_paciente)  # Busca el paciente por ID
    if paciente:
        db.session.delete(paciente)  # Elimina el paciente
        db.session.commit()  # Confirma los cambios en la base de datos
        return jsonify({'message': 'Paciente eliminado correctamente'})
    else:
        return jsonify({'message': 'Paciente no encontrado'})