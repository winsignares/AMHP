#https://docs.sqlalchemy.org/en/14/core/type_basics.html
#https://flask.palletsprojects.com/en/2.2.x/
#from api.user import *
from flask import Flask,  redirect, request, jsonify, json, session, render_template,url_for
from config.db import db, app, ma




#estas son las dependencias del proyecto como flask y ect... 
import os
import time
import threading
import signal
import sys
import subprocess
import pkg_resources
# Códigos de colores
ERROR_COLOR = '\033[91m'
SUCCESS_COLOR = '\033[92m'
END_COLOR = '\033[0m'

# Línea de separación
SEPARATOR_LINE = '-' * 50

def verificar_instalacion_virtualenv():
    print(f'{SEPARATOR_LINE}\nPaso 1\n{SEPARATOR_LINE}')
    print('Verificando la instalación de virtualenv por 5 segundos...')
    time.sleep(5)
    try:
        output = os.popen('pip show virtualenv').read()
        if output:
            print(f'{SUCCESS_COLOR}El paso 1 ya está completado.{END_COLOR}')
        else:
            print(f'{ERROR_COLOR}Instalando virtualenv...{END_COLOR}')
            ruta_instalacion = os.path.join(os.getcwd(), 'env') # Ruta de instalación en la carpeta principal
            os.system(f'pip install virtualenv --target={ruta_instalacion}')
            print(f'{SUCCESS_COLOR}El paso 1 se completó correctamente.{END_COLOR}')
    except Exception as e:
        print(f'{ERROR_COLOR}Ocurrió un error al verificar la instalación:{END_COLOR}')
        print(e)

def verificar_entorno_virtual():
    print(f'{SEPARATOR_LINE}\nPaso 2\n{SEPARATOR_LINE}')
    print(f'{SUCCESS_COLOR}Verificando el entorno virtual por 5 segundos...{END_COLOR}')
    time.sleep(5)
    env_folder = os.path.join(os.path.dirname(os.getcwd()), 'env')
    if not os.path.exists(env_folder):
        print(f'{ERROR_COLOR}No se encontró el entorno virtual.{END_COLOR}')
        print(f'{ERROR_COLOR}Creando el entorno virtual...{END_COLOR}')
        os.system(f'virtualenv {env_folder}')
        print(f'{SUCCESS_COLOR}El entorno virtual se creó correctamente.{END_COLOR}')
    else:
        print(f'{SUCCESS_COLOR}El paso 2 ya está completado.{END_COLOR}')

def activar_entorno_virtual():
    print(f'{SEPARATOR_LINE}\nPaso 3\n{SEPARATOR_LINE}')
    print(f'{SUCCESS_COLOR}Activando el entorno virtual...{END_COLOR}')

    activate_script = os.path.join(os.path.dirname(os.getcwd()), 'env', 'Scripts', 'activate.bat')
    subprocess.call(activate_script, shell=True)

    # Verificar si el entorno virtual se activó correctamente
    if 'VIRTUAL_ENV' in os.environ:
        print(f'{SUCCESS_COLOR}El entorno virtual se activó correctamente.{END_COLOR}')
    else:
        print(f'{ERROR_COLOR}No se está activo.{END_COLOR}')
        print(f'{SUCCESS_COLOR}Activando...{END_COLOR}')
        subprocess.call(activate_script, shell=True)
        print(f'{SUCCESS_COLOR}Activación exitosa{END_COLOR}')

def verificar_dependencias():
    print(f'{SEPARATOR_LINE}\nPaso 4\n{SEPARATOR_LINE}')
    print('Verificando la instalación de las dependencias esenciales...')
    dependencies = [
        'flask', 'flask-sqlalchemy', 'flask-marshmallow',
        'marshmallow', 'pymysql'
    ]
    
    for dependency in dependencies:
        print(f'Verificando {dependency}...')
        try:
            output = os.popen(f'pip show {dependency}').read()
            if output:
                print(f'{SUCCESS_COLOR}{dependency} está instalado.{END_COLOR}')
            else:
                print(f'{ERROR_COLOR}{dependency} no está instalado.{END_COLOR}')
                print(f'{SUCCESS_COLOR}Instalando {dependency}...{END_COLOR}')
                os.system(f'pip install {dependency}')
                print(f'{SUCCESS_COLOR}{dependency} se instaló correctamente.{END_COLOR}')
        except Exception as e:
            print(f'{ERROR_COLOR}Ocurrió un error al verificar {dependency}:{END_COLOR}')
            print(e)

def input_with_timeout(prompt, timeout):
    result = [None]
    event = threading.Event()

    def input_thread():
        try:
            result[0] = input(prompt)
        except EOFError:
            pass
        finally:
            event.set()

    input_thread = threading.Thread(target=input_thread)
    input_thread.start()

    event.wait(timeout) 

    return result[0]

def paso_4():
    print(f'{SEPARATOR_LINE}\nPaso 5-Anexo de Dependencia\n{SEPARATOR_LINE}')
    print('¿Deseas agregar otras dependencias? (Sí/No)')
    answer = input_with_timeout('> ', 5)

    if answer is None:
        print(f'{SUCCESS_COLOR}No se proporcionó ninguna respuesta. Pasando al siguiente paso.{END_COLOR}')
        return

    if answer.lower() == 'sí' or answer.lower() == 'si':
        print('¿Cuántas dependencias deseas agregar?')
        try:
            num_dependencies = int(input_with_timeout('> ', 5))
            for i in range(num_dependencies):
                print(f'Ingresa el nombre de la dependencia #{i+1}:')
                dependency_name = input_with_timeout('> ', 5)
                print(f'{SUCCESS_COLOR}Instalando {dependency_name}...{END_COLOR}')
                os.system(f'pip install {dependency_name}')
                print(f'{SUCCESS_COLOR}{dependency_name} se instaló correctamente.{END_COLOR}')
        except (TypeError, ValueError):
            print(f'{ERROR_COLOR}Respuesta inválida. Pasando al siguiente paso.{END_COLOR}')
    else:
        print(f'{SUCCESS_COLOR}No se agregaron dependencias adicionales. Pasando al siguiente paso.{END_COLOR}')

def verificar_requirements():
    required_libraries = [
        'flask==2.0.1',
        'flask-sqlalchemy==2.5.1',
        'flask-marshmallow==0.15.1',
        'marshmallow==3.13.0',
        'pymysql==1.0.2'
    ]

    librerias_faltantes = []
    for libreria in required_libraries:
        libreria_nombre, libreria_version = libreria.split('==')
        try:
            __import__(libreria_nombre)
        except ImportError:
            librerias_faltantes.append(libreria)

    if librerias_faltantes:
        print('Faltan las siguientes librerías requeridas:')
        for libreria in librerias_faltantes:
            print(libreria)
        generar_requirements_txt(librerias_faltantes)
        print('Instalando las dependencias desde requirements.txt...')
        os.system('pip install -r requirements.txt')
    else:
        print('Todas las librerías requeridas ya están instaladas.')

def generar_requirements_txt(librerias_faltantes):
    ruta_proyecto = os.path.dirname(os.path.abspath(__file__))
    ruta_requirements = os.path.join(ruta_proyecto, '..', 'requirements.txt')
    with open(ruta_requirements, 'w') as file:
        for libreria in librerias_faltantes:
            file.write(libreria + '\n')

def handle_interrupt(signal, frame):
    print(f'\n{ERROR_COLOR}La ejecución del programa fue interrumpida.{END_COLOR}')
    os._exit(1)

signal.signal(signal.SIGINT, handle_interrupt)

verificar_instalacion_virtualenv()

# Verificar el entorno virtual
verificar_entorno_virtual()

# Activar el entorno virtual
activar_entorno_virtual()

# Verificar las dependencias
verificar_dependencias()

# Paso 4 - Anexo de Dependencia
paso_4()

# Verificar las dependencias nuevamente
verificar_requirements()






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
    
    
    
    
    
    
    


