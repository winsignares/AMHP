from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from flask_sqlalchemy import SQLAlchemy


routes_home = Blueprint("routes_home", __name__)


@routes_home.route("/indexcita",  methods=['GET'])
def indexcita():
    titulo = "Pagina cita"
    return render_template('/main/savecita_user.html', titles=titulo)

@routes_home.route("/indexadmin_tabla_medico" )
def indexadmin_tabla_medico():
    titulo= "Pagina admin_tabla_medico"
    return render_template('/main/admin_tabla_medico.html', titles=titulo)

@routes_home.route("/indexadmin_tabla_paciente" )
def indexadmin_tabla_paciente():
    titulo= "Pagina admin_tabla_paciente"
    return render_template('/main/admin_tabla_paciente.html', titles=titulo)



@routes_home.route("/indexcontacto" )
def indexblanqueamentos():
    titulo= "Pagina blanqueamentos"
    return render_template('/main/contacto.html', titles=titulo)

@routes_home.route("/indexcalendario" )
def indexcalenda():
    titulo= "Pagina calendario_admin"
    return render_template('/main/calendario_admin.html', titles=titulo)


@routes_home.route("/indexsobre" )
def indeximplantes():
    titulo= "Pagina implantes"
    return render_template('/main/sobre.html', titles=titulo)


@routes_home.route("/indexprincipal" )
def indexprincipal():
    titulo= "Pagina principal"
    return render_template('/main/principal.html', titles=titulo)


@routes_home.route("/indexlogin" )
def indexlogin():
    titulo= "Pagina login"
    return render_template('/main/login_admin.html', titles=titulo)



@routes_home.route("/tablauser" )
def indexcitauser():
    titulo= "Pagina tabla user"
    return render_template('/main/tabla_cita_user.html', titles=titulo)



@routes_home.route("/indexservice" )
def indexortodoncias():
    titulo= "Pagina ortodoncias"
    return render_template('/main/service.html', titles=titulo) 



@routes_home.route("/indexregistro" )
def indexregistro():
    titulo= "Pagina registro"
    return render_template('/main/registro_user.html', titles=titulo)




@routes_home.route("/indexcita2" )
def indexcita2():
    titulo= "Pagina cita2"
    return render_template('/main/tablaadmin.html', titles=titulo)


@routes_home.route("/indexregistroadmin" )
def jjjjjj():
    titulo= "Pagina registroadmin"
    return render_template('/main/registro_admin.html', titles=titulo)