from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.paciente import pacientes

routes_principal = Blueprint("routes_principal", __name__)


@routes_principal.route("/indexprincipal" )
def indexprincipal():
    titulo= "Pagina principal"
    return render_template('/main/principal.html', titles=titulo)