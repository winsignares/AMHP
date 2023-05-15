from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from flask_sqlalchemy import SQLAlchemy


routes_home = Blueprint("routes_home", __name__)


@routes_home.route("/indexcita",  methods=['GET'])
def indexcita():
    titulo = "Pagina cita"
    return render_template('/main/savecita_user.html', titles=titulo)

@routes_home.route("/indexadmin_tabla_medico" )
def indexadmin_tabla_medico():
    titulo= "Pagina admin_tabla_medico"
    return render_template('/main/admin_tabla_medico.html', titles=titulo)

@routes_home.route("/indexadmin_tabla_paciente" )
def indexadmin_tabla_paciente():
    titulo= "Pagina admin_tabla_paciente"
    return render_template('/main/admin_tabla_paciente.html', titles=titulo)



@routes_home.route("/indexblanqueamentos" )
def indexblanqueamentos():
    titulo= "Pagina blanqueamentos"
    return render_template('/main/blanqueamentos.html', titles=titulo)