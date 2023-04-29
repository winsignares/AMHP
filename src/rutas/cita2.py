from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.paciente import pacientes

routes_cita2 = Blueprint("routes_cita2", __name__)


@routes_cita2.route("/indexcita2" )
def indexcita2():
    titulo= "Pagina cita2"
    return render_template('/main/cita2.html', titles=titulo)