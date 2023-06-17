# AMHP
Cree mi entorno virtual -virtualenv -p python3 env

Activar entorno virtual -. env/Scripts/activate ya dentro del entorno virtual

Ejecutar pip list o pip freeze para listar los paquetes que tenemos instalados hasta ahora en nuestro entorno virtual.

Instale flask en mi entorno virtual y demas que aqui abajo estaran 

pip install flask
pip install pyMySQL
pip install SQLAlchemy
pip install Marshmallow

Import modulo pyMySQL ,SQLAlchemy, Marshmallow en el archivo db(ya esta echo)

Crear conexión y hacer pruebas.



Ejecutar archivo requirements.txt solo basta con escribir pip install -r requirements.txt

Para ejecutar el codigo, primero ejecutamos cd src/ luego: py app.py o ejecutando flask run

Nota: No es indispensable instalar: -pip install flask-login para trabajar con login y session, en el paquete werkzeug ya con eso lo podemos importar Para incriptar la clave debo importar from werkzeug.security import generate_password_hash, check_password_hash

En Python, podemos usar los siguientes módulos para comunicarnos con MySQL.(esto es solo otra manera ) 1 MySQL Connector Python 2 PyMySQL 3 MySQLDB ::IMPORTANTE, Recomiendo no usar este Modulo flask_mysqldb 4 MySqlClient 5 OurSQL aunque no se esten utilizando estas solo es sugerencia 


