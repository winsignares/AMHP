from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.odontologo import odontologos

routes_ortodoncias = Blueprint("routes_ortodoncias", __name__)


@routes_ortodoncias.route("/indexortodoncias" )
def indexortodoncias():
    titulo= "Pagina ortodoncias"
    return render_template('/main/ortodoncias.html', titles=titulo) 


