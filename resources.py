# Regla de oro: Todos los recursos que agreguemos para nuestra aplicación irán en este archivo

from flask_restful import Resource


from flask import render_template, make_response, request


class PrimerRecurso(Resource):
  def get(self):
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


class NombreAleatorio(Resource):
  def get(self):
    stock = 40
    vendidos = 30
    faltantes = 10

    return {'Vendidos': vendidos, 'Faltantaes': faltantes, 'Stock': stock}


class PaginaInicio(Resource):

  # Cuando el usuario acceda a este recurso, vamos a renderizar el sitio web
  def get(self):

    # Renderizamos ese archivo | Convertir de código a una vista
    sitio_web_renderizado = render_template('pagina_1.html')

    # Le decimos a python que le muestre la vista como respuesta
    return make_response(sitio_web_renderizado)


class PaginaPreguntas(Resource):

  # Cuando el usuario acceda a este recurso, vamos a renderizar el sitio web
  def get(self):

    # Renderizamos ese archivo | Convertir de código a una vista
    sitio_web_renderizado = render_template('pagina_2.html')

    # Le decimos a python que le muestre la vista como respuesta
    return make_response(sitio_web_renderizado)


# Creamos el recurso al cual el usuario va a acceder
class Login(Resource):

  # El método que se ejecutará cuando el usuario acceda al recurso
  def get(self):

    # Renderizamos ese archivo | Convertir de código a una vista
    sitio_web_renderizado = render_template('login.html')

    # Le decimos a python que le muestre la vista como respuesta
    return make_response(sitio_web_renderizado)

  def post(self):

    # Almacenaremos la información que el usuario nos envie
    info_usuario = request.form.get('email')
    password_usuario = request.form.get('password')

    return {'Correo': info_usuario, 'Password': password_usuario}
