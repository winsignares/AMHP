from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from flask_sqlalchemy import SQLAlchemy
from model.fechas_disponibles import   fechas_disponi

routes_fecha_disponible = Blueprint("routes_fecha_disponible", __name__)



@routes_fecha_disponible.route('/mostrar_fecha_dispo_tabla', methods=['GET'])
def mostarfechadispotabla():
    datos= {}
    resultado = db.session.query(fechas_disponi).select_from(fechas_disponi).all()
    i=0
    goria = []
    for fecha in resultado:
        i+=1	        
        datos[i] = {
        'id':fecha.id,
        'fechas_dispon':fecha.fechas_dispon
                                                   
        }
        goria.append(datos)
    return jsonify(datos)


@routes_fecha_disponible.route('/eliminar_fecha_disponi_tabla', methods=['POST'])
def eliminar_paciente_admin():
    # Obtener el ID del paciente a eliminar desde la solicitud POST
    id_fecha_dis = request.json['id']

    # Lógica para eliminar el paciente en la base de datos
    # Aquí debes escribir el código para eliminar el paciente utilizando la biblioteca o método que estés utilizando para interactuar con la base de datos
    
    fecha_dispo = fechas_disponi.query.get(id_fecha_dis)  # Busca el paciente por ID
    if fecha_dispo:
        db.session.delete(fecha_dispo)  # Elimina el paciente
        db.session.commit()  # Confirma los cambios en la base de datos
        return jsonify({'message': 'fecha eliminado correctamente'})
    else:
        return jsonify({'message': 'fecha no encontrado'})