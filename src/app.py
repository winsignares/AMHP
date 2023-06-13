#https://docs.sqlalchemy.org/en/14/core/type_basics.html
#https://flask.palletsprojects.com/en/2.2.x/
#from api.user import *
from flask import Flask,  redirect, request, jsonify, json, session, render_template,url_for
from config.db import db, app, ma




#importar los model en orden
from model.admin import admins
from model.paciente import pacientes
from model.odontologo import odontologos

from model.histo_clinico import histoclinicos
from model.fechas_disponibles import  fechas_disponi

from model.cita import citas

from model.tratamiento import tratamientos





# importar rutas
from rutas.save_cita_user import routes_cita_user
from rutas.registro import routes_registro
from rutas.tabla_cita_admin import routes_cita_admin
from rutas.login import routes_login
from rutas.mostrarcitas_user import routes_mos_user
from rutas.admin_tabla_paciente import routes_admin_tabla_paciente
from rutas.admin_tabla_medico import routes_admin_tabla_medico
from rutas.admin_tabla_medico import routes_admin_tabla_medico
from rutas.fecha_disponible import routes_fecha_disponible


#importar la ruta hoome 
from rutas.home import routes_home
#importar el home todas las rutas de las viustas del servidor
app.register_blueprint(routes_home , url_prefix="/fronted")


# import bluplint
app.register_blueprint(routes_cita_user, url_prefix="/fronted")
app.register_blueprint(routes_registro, url_prefix="/fronted")
app.register_blueprint(routes_cita_admin, url_prefix="/fronted")
app.register_blueprint(routes_login , url_prefix="/fronted")
app.register_blueprint(routes_mos_user , url_prefix="/fronted")
app.register_blueprint(routes_admin_tabla_paciente , url_prefix="/fronted")
app.register_blueprint(routes_admin_tabla_medico , url_prefix="/fronted")
app.register_blueprint(routes_fecha_disponible , url_prefix="/fronted")





@app.route('/logout')
def logout():
    # Eliminar datos de sesión, esto cerrará la sesión del usuario
    session.pop('conectado', None)
    session.pop('admin_id', None)
    session.pop('admin_nombre', None)
    
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(error):
    if 'conectado' in session:
        return redirect(url_for('index'))
    else:
        return render_template('/main/principal.html')
    
    
@app.route("/")
def index():
    titulo= "Pagina Princiapl"
    return render_template('/main/principal.html', titles=titulo)




#esto para que corra el server y ayuda con el puerto
if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')