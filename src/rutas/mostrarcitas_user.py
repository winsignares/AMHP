from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.cita import citas
from model.registro import registro

routes_mos_user = Blueprint("routes_mos_user", __name__)


@routes_mos_user.route("/tablauser" )
def indexcita2():
    titulo= "Pagina tabla user"
    return render_template('/main/prueba_mostrar_user.html', titles=titulo)


@routes_mos_user.route('/mostrar_citas', methods=['GET'] )
def actualizar_citas():
    datos= {}
    #resultado = db.session.query(citas,registro).select_from(citas).join(registro).filter(id=id).all()
    cursor = db.cursor()
    cursor.execute("SELECT Nombre_completo ,Edad,Username FROM tblcitas s join tblregistro d on s.id =d.id ")  # select * from cita join registro on cita.id = registro.id_cita
    resultado = cursor.fetchall()  #  [(1, 'joel', 'joel@mail.com', '123456789'),
    # i=0
    # goria = []
    # for cate in resultado:
    #     i+=1	       
    #     datos[i] = {
    #     'id':cate.id,
	# 	'Nombre_completo':cate.Nombre_completo,
	# 	'Edad':cate.Edad,                                                    
	# 	'Username':cate.Username,                                                                                                        
    #     }
    #     goria.append(datos)
    # return jsonify(datos)
    
#########################
# db = MySQLdb.connect(app.config['MYSQL_HOST'], app.config['MYSQL_USER'], app.config['MYSQL_PASSWORD'], app.config['MYSQL_DB'])
#     cursor = db.cursor()
#     cursor.execute("SELECT * FROM tabla")
#     results = cursor.fetchall()
#     return render_template('index.html', results=results)

@routes_mos_user.route('/updatesolicitudes', methods=['POST'] )
def actualizarS():
    id = request.json['id']
    solicitudes = request.json['Nombre_proveedor','Telefono','Direccion','Descripcion']
    pusuario = solicitudes.query.get(id)
    pusuario.cantidad = solicitudes
    db.session.commit()
    return redirect('/updatesolicitudes')


