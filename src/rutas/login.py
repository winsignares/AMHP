from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.admin import admins


routes_login = Blueprint("routes_login", __name__)


@routes_login.route("/login", methods=["POST"])
def validar_login():
  
    usuario = request.json["usuario"]
    contraseña = request.json["contraseña"]
    verificacion = db.session.query(admins).filter(admins.usuario == usuario,admins.contraseña == contraseña,).first()

    # Busca el usuario en la base de datos
    if verificacion:  
        return "Correcto"