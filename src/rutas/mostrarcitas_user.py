from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.cita import citas 
from model.registro import registro

routes_mos_user = Blueprint("routes_mos_user", __name__)


@routes_mos_user.route("/tablauser" )
def indexcita2():
    titulo= "Pagina tabla user"
    return render_template('/main/tabla_cita_user.html', titles=titulo)


# @routes_mos_user.route('/mostrar_citas', methods=['GET'] )
# def actualizar_citas():

#     datos= {}
#     resultado = db.session.query(registro,citas).join(registro,citas.id == registro.id).all()
#     i=0
#     goria = []
#     for cate in resultado:
#         i+=1	       
#         datos[i] = {
#         'id':cate.id,
# 		'Name':cate.Name,
# 		'Username':cate.Username,                                                    
# 		'Nombre_completo':cate.Nombre_completo,                                                                                                    
#         }
#         goria.append(datos)
#     return jsonify(datos)



    # db = db.connect(app.config['MYSQL_HOST'], app.config['MYSQL_USER'], app.config['MYSQL_PASSWORD'], app.config['MYSQL_DB'])
    # cursor = db.cursor()
    # cursor.execute("SELECT * FROM tabla")
    # results = cursor.fetchall()
    # return render_template('index.html', results=results)