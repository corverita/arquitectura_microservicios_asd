# -*- coding: utf-8 -*-
# !/usr/bin/env python
# ----------------------------------------------------------------------------------------------------------------
# Archivo: app.py
#
# Implementación de Arquitecturas Micro Servicios.
# Autor(es): Perla Velasco & Jorge Alfonso Solís.
# Version: 1.0.0 Marzo 2021
#
# Descripción:
#
#   Este archivo define un ejemplo sencillo de un micro servicio desarrollado en el lenguaje de programación Python.
#   
#                                             app.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |  - Envía un mensaje     | - Utiliza el frame-    |
#           |     HelloResource     |    al ser llamada       |   work de desarrollo   |
#           |                       |    mediante el método   |   Falcon para su im-   |
#           |                       |    get.                 |   plementación.        |
#           +-----------------------+-------------------------+------------------------+
#

import json
import falcon
from falcon_cors import CORS


class HelloResource(object):

    # Método que se llama mediante una solicitud de tipo GET
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({"Message": "Hello World from Python!"})

# Se define la variable cors asignando valores para el middleware
cors = CORS(allow_all_origins=True,
            allow_all_headers=True,
            allow_all_methods=True,
            allow_credentials_all_origins=True)

# Se crea la variable api que representa la API en Falcon
api = application = falcon.API(middleware=[cors.middleware])

# Se asigna la ruta de entrada a la API y la clase que dará respuesta
api.add_route('/hello', HelloResource())
