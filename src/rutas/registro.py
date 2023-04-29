from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.paciente import pacientes

routes_registro = Blueprint("routes_registro", __name__)
routes_ = Blueprint("routes_login", __name__)


@routes_registro.route("/indexregistro" )
def indexregistro():
    titulo= "Pagina registro"
    return render_template('/main/registro.html', titles=titulo)

@routes_registro.route("/indexlogin" )
def indexlogin():
    titulo= "Pagina login"
    return render_template('/main/login.html', titles=titulo)