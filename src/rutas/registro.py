from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.registro import registro


routes_registro = Blueprint("routes_registro", __name__)


@routes_registro.route("/indexregistro" )
def indexregistro():
    titulo= "Pagina registro"
    return render_template('/main/registro_user.html', titles=titulo)


@routes_registro.route('/guardaregistro', methods=['POST'])
def saveregistro():

    Name = request.form['Name']
    Username = request.form['Username']
    Email = request.form['Email']
    Password = request.form['Password']
    print(Name)
    new_reg = registro(Name,Username,Email,Password)
    db.session.add(new_reg)
    db.session.commit()
    return "si"
