from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.paciente import pacientes

routes_index = Blueprint("routes_index", __name__)


@routes_index.route("/indexindex" )
def indexindex():
    titulo= "Pagina index"
    return render_template('/main/index.html', titles=titulo)