from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
# from model.paciente import pacientes

routes_admin_tabla_paciente = Blueprint("routes_admin_tabla_paciente", __name__)


@routes_admin_tabla_paciente.route("/indexadmin_tabla_paciente" )
def indexadmin_tabla_paciente():
    titulo= "Pagina admin_tabla_paciente"
    return render_template('/main/admin_tabla_paciente.html', titles=titulo)