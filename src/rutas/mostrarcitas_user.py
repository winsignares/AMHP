from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.cita import citas
from model.registro import registro

routes_mos_user = Blueprint("routes_mos_user", __name__)


@routes_mos_user.route("/tablauser" )
def indexcita2():
    titulo= "Pagina tabla user"
    return render_template('/main/prueba_mostrar_user.html', titles=titulo)