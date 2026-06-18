from flask import Flask  # Nos permite convertir nuestra PC en un servidor web

# Nos permite crear una API REST de manera sencilla y con estructura de POO
from flask_restful import Api

# Importamos las rutas para inicializarlas
from routes import AdministradorDeRutas


app = Flask(__name__)  # Creamos un servidor y lo guardamos en la variable app

# Creamos el motor que hace funcionar al servidor, lo guardamos en la variable api
api = Api(app)

# Objeto que controle todas mis rutas
rutas = AdministradorDeRutas()
rutas.inicializar_rutas(api)
# Vamos a inicializar las rutas...


# Quiero que LEVANTES=PONERLO A CORRER ese servidor en formato "desarrollo" y en el puerto 8000
app.run(debug=True, port=8000)
