from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.fechas_disponibles import fechas_dispo


routes_fechasdisplo = Blueprint("routes_fechasdisplo", __name__)



@routes_fechasdisplo.route('/ingresar_fechas_disponibles', methods=['POST'])
def savecita_adminsssss():


    fechas_dispon = request.form['fechas_dispon']

    # problema = date.today()
   
    new_cit = fechas_dispo(fechas_dispon)
    db.session.add(new_cit)
    db.session.commit()
    return "si" 
