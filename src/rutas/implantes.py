from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.paciente import pacientes

routes_implantes = Blueprint("routes_implantes", __name__)


@routes_implantes.route("/indeximplantes" )
def indeximplantes():
    titulo= "Pagina implantes"
    return render_template('/main/implantes.html', titles=titulo)