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

from flask import Flask, render_template, redirect, jsonify, json, request
import json, requests
from flask.helpers import url_for
from flask import request
from flask_cors import CORS
from flask import jsonify

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
# @app.route("/", defaults={'api': None}, methods=['GET'])
# @app.route("/<api>", methods=['GET'])
# def index(api):

#     # Se verifica si se recibió la variable api
#     if api:

#         if int(api) == 1:
#             # Se llama al microservicio enviando como parámetro la url y el header
#             ms1 = requests.get(url_microservice1, headers=headers_m1)
#             # Se convierte la respuesta a json
#             json = ms1.json()
#             # Se crea el json que será enviado al template
#             json_result = {'ms1': json}
#         elif int(api) == 2:
#             # Se llama al microservicio enviando como parámetro la url y el header
#             ms2 = requests.get(url_microservice2, headers=header_m2)
#             # Se convierte la respuesta a json
#             json = ms2.json()
#             # Se crea el json que será enviado al template
#             json_result = {'ms2': json}
#         elif int(api) == 3:
#             # Se llama al microservicio enviando como parámetro la url y el header 
#             ms3 = requests.get(url_microservice3, headers=header_m3)
#             # Se convierte la respuesta a json
#             json = ms3.json()
#             # Se crea el json que será enviado al template
#             json_result = {'ms3': json}
#         elif int(api) == 4:
#             # Se llama al microservicio enviando como parámetro la url y el header 
#             ms4 = requests.get(url_microservice4, headers=header_m4)
#             # Se convierte la respuesta a json
#             json = ms4.json()
#             # Se crea el json que será enviado al template
#             json_result = {'ms4': json}
#         elif int(api) == 5:
#             # Se llama al microservicio enviando como parámetro la url y el header 
#             ms5 = requests.get(url_microservice5, headers=header_m5)
#             # Se convierte la respuesta a json
#             json = ms5.json()
#             # Se crea el json que será enviado al template
#             json_result = {'ms5': json}
        
#         return render_template("index.html", result=json_result)
    
#     # Si no se recibe, simplemente se regresa el template index.html sin datos.
#     else:
#         json_result = {}
#         return render_template("index.html", result=json_result)

@app.route("/", methods=['GET'])
def list():
    respuesta = requests.get('http://host.docker.internal:8080/catalog/product', headers=header_m4)
    return render_template("list.html", result=respuesta.json())

@app.route("/catalog/product/<id>/", methods=['GET','POST'])
def detail(id):
    if request.method=="POST":
        data=request.json
        print(data)
        respuesta= requests.post('http://host.docker.internal:8080/catalog/product/cart/', headers=header_m4, data=data)
        print(respuesta)
        return redirect(url_for("list"))
    respuesta = requests.get('http://host.docker.internal:8080/catalog/product/'+id+'/', headers=header_m4)
    return render_template("detail.html", result=respuesta.json())

@app.route("/orders/order/", methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        carrito=requests.get('http://host.docker.internal:8080/catalog/product/cart/', headers=header_m4)
        json_carrito=carrito.json()
        suma_carrito=0.0
        cantidad=0
        for product in json_carrito:
            suma_carrito+=float(product['total_product'])
            cantidad+=1

        orden = requests.post('http://host.docker.internal:8080/orders/order/get/', headers=header_m5, data=request.form)
        json=orden.json()
        sum=0.0
        for product in json:
            sum+=float(product['total_item_price'])
        data={
            "json":json,
            "total":sum,
            "sum_cart":suma_carrito,
            "quantity_cart":cantidad
        }
        return render_template('orders.html', result=data)
    return render_template("order_form.html")

@app.route("/cart/", methods=['GET', 'POST'])
def cart():
    carrito=requests.get('http://host.docker.internal:8080/catalog/product/cart/', headers=header_m4)
    carrito_json=carrito.json()
    suma_carrito=0.0
    cantidad=0
    for product in carrito_json:
        suma_carrito+=float(product['total_product'])
        cantidad+=1
    data={
        "quantity_cart":cantidad,
        "sum_cart":suma_carrito,
        "cart_items":carrito_json
    }
    return render_template("cart/detail.html", result=data)


@app.route("/cart/remove/", methods=['POST'])
def cart_delete():
    product_id = request.form['product_id']
    data = {
        "product_id":product_id
    }
    carrito_remove = requests.delete('http://host.docker.internal:8080/catalog/product/cart/', headers=header_m4, data=data)
    print(carrito_remove)
    carrito=requests.get('http://host.docker.internal:8080/catalog/product/cart/', headers=header_m4)
    carrito_json=carrito.json()
    suma_carrito=0.0
    cantidad=0
    for product in carrito_json:
        suma_carrito+=float(product['total_product'])
        cantidad+=1
    data_env={
        "quantity_cart":cantidad,
        "sum_cart":suma_carrito,
        "cart_items":carrito_json
    }
    return render_template("cart/detail.html", result=data_env)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')