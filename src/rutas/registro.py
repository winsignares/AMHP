from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.paciente import pacientes
from datetime import datetime,date


routes_registro = Blueprint("routes_registro", __name__)



@routes_registro.route('/guardaregistro', methods=['GET', 'POST'])
def saveregistro():
    Rol = "user" 
    fecha_registro = date.today()
    Name = request.form['Name']
    edad = request.form['edad']
    cedula = request.form['cedula']
    telefono = request.form['telefono']
    direccion = request.form['direccion']
    Email = request.form['Email']
    fecha_nacimiento = request.form['fecha_nacimiento']
    
    
    # Check if the patient already exists in the database
    existing_patient = pacientes.query.filter(
        (pacientes.cedula == cedula) | (pacientes.Email == Email)
    ).first()
    if existing_patient:
        return "Paciente already exists in the database"
    
    new_reg = pacientes(Rol,fecha_registro,Name,edad, cedula, telefono, direccion, Email, fecha_nacimiento)
    db.session.add(new_reg)
    db.session.commit()
    return "Registro exitoso" 
 