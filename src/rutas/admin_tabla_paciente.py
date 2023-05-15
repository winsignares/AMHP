from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.paciente import pacientes

routes_admin_tabla_paciente = Blueprint("routes_admin_tabla_paciente", __name__)



@routes_admin_tabla_paciente.route('/guardarpaciente_admin', methods=['POST']) 
def saveregistro_admin():
    Name = request.form['Name']
    cedula = request.form['cedula']
    telefono = request.form['telefono']
    direccion = request.form['direccion']
    Email = request.form['Email']
    fecha_nacimiento = request.form['fecha_nacimiento']
    print(Name)
    new_reg = pacientes(Name,cedula,telefono,direccion,Email,fecha_nacimiento)
    db.session.add(new_reg)
    db.session.commit()
    return "si"


@routes_admin_tabla_paciente.route('/eliminar_paciente_admin', methods=['POST'])
def eliminar_paciente_admin():
    # Obtener el ID del paciente a eliminar desde la solicitud POST
    id_paciente = request.json['id']

    # Lógica para eliminar el paciente en la base de datos
    # Aquí debes escribir el código para eliminar el paciente utilizando la biblioteca o método que estés utilizando para interactuar con la base de datos
    
    paciente = pacientes.query.get(id_paciente)  # Busca el paciente por ID
    if paciente:
        db.session.delete(paciente)  # Elimina el paciente
        db.session.commit()  # Confirma los cambios en la base de datos
        return jsonify({'message': 'Paciente eliminado correctamente'})
    else:
        return jsonify({'message': 'Paciente no encontrado'})
    
@routes_admin_tabla_paciente.route('/mostrar_pacientes_admin', methods=['GET'])
def mostarpaciente_admin():
    datos= {}
    resultado = db.session.query(pacientes).select_from(pacientes).all()
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



@routes_admin_tabla_paciente.route('/actualizar_paciente_admin', methods=['POST'] )
def actualizar_paciente():
  # Obtener los datos enviados en la solicitud
    id = request.form.get('id')
    name = request.form.get('Name')
    cedula = request.form.get('cedula')
    telefono = request.form.get('telefono')
    direccion = request.form.get('direccion')
    email = request.form.get('Email')
    fecha_nacimiento = request.form.get('fecha_nacimiento')

    # Aquí puedes realizar las operaciones necesarias para actualizar los datos en la base de datos
    # por ejemplo, usando un ORM como SQLAlchemy o ejecutando consultas directas a la base de datos

    # Ejemplo de actualización usando SQLAlchemy
    paciente = pacientes.query.get(id)
    paciente.Name = name
    paciente.cedula = cedula
    paciente.telefono = telefono
    paciente.direccion = direccion
    paciente.Email = email
    paciente.fecha_nacimiento = fecha_nacimiento

    # Guardar los cambios en la base de datos
    db.session.commit()
      
    # Enviar una respuesta exitosa
    return jsonify({'message': 'Datos actualizados correctamente'})
