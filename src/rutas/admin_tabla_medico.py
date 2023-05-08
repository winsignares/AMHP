from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
# from model.paciente import pacientes

routes_admin_tabla_medico = Blueprint("routes_admin_tabla_medico", __name__)


@routes_admin_tabla_medico.route("/indexadmin_tabla_medico" )
def indexadmin_tabla_medico():
    titulo= "Pagina admin_tabla_medico"
    return render_template('/main/admin_tabla_medico.html', titles=titulo)