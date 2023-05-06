from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.registro import registros


routes_registro = Blueprint("routes_registro", __name__)


@routes_registro.route("/indexregistro" )
def indexregistro():
    titulo= "Pagina registro"
    return render_template('/main/registro_user.html', titles=titulo)


@routes_registro.route('/guardaregistro', methods=['POST'])
def saveregistro():
    print("hola")
    Name = request.form['Name']
    cedula = request.form['cedula']
    telefono = request.form['telefono']
    direccion = request.form['direccion']
    Email = request.form['Email']
    fecha_nacimiento = request.form['fecha_nacimiento']
    print(Name)
    new_reg = registro(Name,cedula,telefono,direccion,Email,fecha_nacimiento)
    db.session.add(new_reg)
    db.session.commit()
    return "si"
