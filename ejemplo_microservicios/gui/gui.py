# -*- coding: utf-8 -*-
# !/usr/bin/env python
# ----------------------------------------------------------------------------------------------------------------
# Archivo: gui.py
# Implementación de Arquitecturas Micro Servicios.
# Autor(es): Perla Velasco & Jorge Alfonso Solís.
# Version: 1.0 Marzo 2021
# Descripción:
#
#   Este archivo define la interfaz gráfica del usuario. Recibe un parámetro que define el 
#   Microservicio que se desea utilizar.
#   
#                                             gui.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |  - Porporcionar la in-  | - Consume servicios    |
#           |          GUI          |    terfaz gráfica con la|   para proporcionar    |
#           |                       |    que el usuario hará  |   información al       |
#           |                       |    uso del sistema.     |   usuario.             |
#           +-----------------------+-------------------------+------------------------+
#

from flask import Flask, render_template
import json, requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Se definen las llaves de cada microservicio

key_m1 = "<microservice1_key>"
headers_m1 = {"authorization": key_m1}

key_m2 = "377bc3711ebf47d29f638c291c11aaa9"
header_m2 = {"authorization": key_m2}

key_m3 = "<microservice3_key>"
header_m3 = {"authorization": key_m3}

key_m4 = "5740799c5a004461ab68c30552796218"
header_m4 = {"authorization": key_m4}

key_m5 = "771cf970112d446b95fce6e68069edb4"
header_m5 = {"authorization": key_m5}


# Se definen las url para cada micro servicio.
# Se reemplaza el 127.0.0.1 del localhost por host.docker.internal para hacer la conexión
# con los microservicios dentro de los contenedores de Docker.

# Url para el microservicio 1
url_microservice1 = 'http://host.docker.internal:8080/hello/python'
# Url para el microservicio 2
url_microservice2 = 'http://host.docker.internal:8080/hello/dart'
# Url para el microservicio 3
url_microservice3 = 'http://host.docker.internal:8080/hello/django'
# Url para el microservicio 4 Catalog_service
url_microservice4 = 'http://172.10.0.7:8080/catalog/product'
# Url para el microservicio 5 Orders_service
url_microservice5 = 'http://172.10.0.8:8080/orders/order'


# Método que muestra la página de inicio del sistema
@app.route("/", defaults={'api': None}, methods=['GET'])
@app.route("/<api>", methods=['GET'])
def index(api):

    # Se verifica si se recibió la variable api
    if api:

        if int(api) == 1:
            # Se llama al microservicio enviando como parámetro la url y el header
            ms1 = requests.get(url_microservice1, headers=headers_m1)
            # Se convierte la respuesta a json
            json = ms1.json()
            # Se crea el json que será enviado al template
            json_result = {'ms1': json}
        elif int(api) == 2:
            # Se llama al microservicio enviando como parámetro la url y el header
            ms2 = requests.get(url_microservice2, headers=header_m2)
            # Se convierte la respuesta a json
            json = ms2.json()
            # Se crea el json que será enviado al template
            json_result = {'ms2': json}
        elif int(api) == 3:
            # Se llama al microservicio enviando como parámetro la url y el header 
            ms3 = requests.get(url_microservice3, headers=header_m3)
            # Se convierte la respuesta a json
            json = ms3.json()
            # Se crea el json que será enviado al template
            json_result = {'ms3': json}
        elif int(api) == 4:
            # Se llama al microservicio enviando como parámetro la url y el header 
            ms4 = requests.get(url_microservice4, headers=header_m4)
            # Se convierte la respuesta a json
            json = ms4.json()
            # Se crea el json que será enviado al template
            json_result = {'ms4': json}
        elif int(api) == 5:
            # Se llama al microservicio enviando como parámetro la url y el header 
            ms5 = requests.get(url_microservice5, headers=header_m5)
            # Se convierte la respuesta a json
            json = ms5.json()
            # Se crea el json que será enviado al template
            json_result = {'ms5': json}
        
        return render_template("index.html", result=json_result)
    
    # Si no se recibe, simplemente se regresa el template index.html sin datos.
    else:
        json_result = {}
        return render_template("index.html", result=json_result)

@app.route("/list", methods=['GET'])
def list():
    respuesta = requests.get('http://host.docker.internal:8080/catalog/product', headers=header_m4)
    return render_template("list.html", result=respuesta.json())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')