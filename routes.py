# Regla de oro: Todas las rutas que vayamos a crear en el la app irán en este documento

from resources import *


class AdministradorDeRutas:
  # Este método le dará la pauta a mi aplicación de que rutas vamos a poder usar
  def inicializar_rutas(self, aplicacion):
    aplicacion.add_resource(PrimerRecurso, '/primero')
    aplicacion.add_resource(NombreAleatorio, '/segundo')
    aplicacion.add_resource(PaginaInicio, '/')
    aplicacion.add_resource(PaginaPreguntas, '/faq')
    aplicacion.add_resource(Login, '/login')
    # / -> Ruta Raíz: La primera página que verá el usuario al acceder a nuestra web
