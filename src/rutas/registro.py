from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.paciente import pacientes

routes_registro = Blueprint("routes_registro", __name__)


@routes_registro.route("/indexregistro" )
def indexregistro():
    titulo= "Pagina registro"
    return render_template('/main/registro.html', titles=titulo)