from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.login import login


routes_login = Blueprint("routes_login", __name__)


@routes_login.route("/indexlogin" )
def indexlogin():
    titulo= "Pagina login"
    return render_template('/main/login.html', titles=titulo)