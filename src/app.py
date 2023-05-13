#https://docs.sqlalchemy.org/en/14/core/type_basics.html
#https://flask.palletsprojects.com/en/2.2.x/
#from api.user import *
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma




#importar los model en orden
from model.paciente import pacientes
from model.odontologo import odontologos
from model.admin import admins
# from model.fechas_disponibles import fechas_dispo
from model.histo_clinico import histoclinicos
from model.cita import citas
from model.tratamiento import tratamientos



# importar rutas
from rutas.blanqueamentos import routes_blanqueamentos
from rutas.cita import routes_cita
from rutas.implantes import routes_implantes
from rutas.ortodoncias import routes_ortodoncias
from rutas.registro import routes_registro
from rutas.index import routes_principal
from rutas.tablaadmin import routes_cita2
from rutas.login import routes_login
from rutas.mostrarcitas_user import routes_mos_user
from rutas.calendario import routes_calendario_admin
from rutas.admin_tabla_paciente import routes_admin_tabla_paciente
from rutas.admin_tabla_medico import routes_admin_tabla_medico







# import bluplint
app.register_blueprint(routes_blanqueamentos, url_prefix="/fronted") 
app.register_blueprint(routes_cita, url_prefix="/fronted")
app.register_blueprint(routes_implantes, url_prefix="/fronted")
app.register_blueprint(routes_ortodoncias, url_prefix="/fronted")
app.register_blueprint(routes_registro, url_prefix="/fronted")
app.register_blueprint(routes_principal, url_prefix="/fronted")
app.register_blueprint(routes_cita2, url_prefix="/fronted")
app.register_blueprint(routes_login , url_prefix="/fronted")
app.register_blueprint(routes_mos_user , url_prefix="/fronted")
app.register_blueprint(routes_calendario_admin , url_prefix="/fronted")
app.register_blueprint(routes_admin_tabla_paciente , url_prefix="/fronted")
app.register_blueprint(routes_admin_tabla_medico , url_prefix="/fronted")





@app.route("/")
def index():
    titulo= "Pagina Princiapl"
    return render_template('/main/principal.html', titles=titulo)




#esto para que corra el server y ayuda con el puerto
if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')