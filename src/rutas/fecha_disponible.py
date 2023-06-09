from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from flask_sqlalchemy import SQLAlchemy
from model.fechas_disponibles import   fechas_disponi
from model.cita import citas

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
def eliminar_fecha_disponi_tabla():
    # Obtener el ID de la fecha a eliminar desde la solicitud POST
    id_fecha_dis = request.json['id']

    # Lógica para eliminar la fecha en la base de datos
    fecha_dispo = fechas_disponi.query.get(id_fecha_dis)  # Busca la fecha por ID
    if fecha_dispo:
        # Verificar si hay citas asociadas a la fecha
        citas_fecha = citas.query.filter_by(id_fechadispo=id_fecha_dis).first()
        if citas_fecha:
            return jsonify({'message': 'No se puede eliminar la fecha porque tiene citas asociadas'})

        db.session.delete(fecha_dispo)  # Elimina la fecha
        db.session.commit()  # Confirma los cambios en la base de datos
        return jsonify({'message': 'Fecha eliminada correctamente'})
    else:
        return jsonify({'message': 'Fecha no encontrada'})