from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template



routes_calendario_admin = Blueprint("routes_calendario_admin", __name__)


@routes_calendario_admin.route("/indexcalendario" )
def indexcalenda():
    titulo= "Pagina calendario_admin"
    return render_template('/main/calendario_admin.html', titles=titulo)