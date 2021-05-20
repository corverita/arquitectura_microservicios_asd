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
#           |  Nombre del elemento  |  {{    Responsabilid }}ad     |      Propiedades       |
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

key_m4 = "df5e62340e104cd0b2a23c2739537d05"
header_m4 = {"authorization": key_m4}

key_m5 = "96532f42a6544d3c8978961577386e8d"
header_m5 = {"authorization": key_m5}

# Se definen las url para cada micro servicio.
# Se reemplaza el 127.0.0.1 del localhost por host.docker.internal para hacer la conexión
# con los microservicios dentro de los contenedores de Docker.


# Url para el microservicio 4 Catalog_service
url_microservice4 = 'http://172.10.0.7:8080/catalog/product'
# Url para el microservicio 5 Orders_service
url_microservice5 = 'http://172.10.0.8:8080/orders/order'


@app.route("/", methods=['GET'])
def list():
    carrito=requests.get('http://host.docker.internal:8080/catalog/cart/', headers=header_m4)
    json_carrito=carrito.json()
    suma_carrito=0.0
    cantidad=0
    for product in json_carrito:
        suma_carrito+=float(product['total_product'])
        cantidad+=1
    products = requests.get('http://host.docker.internal:8080/catalog/product', headers=header_m4)
    categories = requests.get('http://host.docker.internal:8080/catalog/categories/', headers=header_m4)
    respuesta = {
        'products':products.json(),
        'categories':categories.json(),
        "sum_cart":suma_carrito,
        "quantity_cart":cantidad
    }

    return render_template("/products/list.html", result=respuesta)

@app.route("/catalog/category/<id>/", methods=['GET'])
def list_id(id):
    carrito=requests.get('http://host.docker.internal:8080/catalog/cart/', headers=header_m4)
    json_carrito=carrito.json()
    suma_carrito=0.0
    cantidad=0
    for product in json_carrito:
        suma_carrito+=float(product['total_product'])
        cantidad+=1
    products = requests.get('http://host.docker.internal:8080/catalog/product/category/'+id+'/', headers=header_m4)
    categories = requests.get('http://host.docker.internal:8080/catalog/categories/', headers=header_m4)
    respuesta = {
        'products':products.json(),
        'categories':categories.json(),
        "sum_cart":suma_carrito,
        "quantity_cart":cantidad
    }
    return render_template("/products/list.html", result=respuesta)

@app.route("/catalog/product/<id>/", methods=['GET','POST'])
def detail(id):
    carrito=requests.get('http://host.docker.internal:8080/catalog/cart/', headers=header_m4)
    json_carrito=carrito.json()
    suma_carrito=0.0
    cantidad=0
    for product in json_carrito:
        suma_carrito+=float(product['total_product'])
        cantidad+=1
    if request.method == 'POST':
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        data = {
            "product_id": product_id,
            "quantity": quantity
        }
        respuesta= requests.post('http://host.docker.internal:8080/catalog/cart/', headers=header_m4, data=data)
        return redirect(url_for("list"))
    respuesta = requests.get('http://host.docker.internal:8080/catalog/product/'+id+'/', headers=header_m4)
    producto=respuesta.json()
    categoria=requests.get('http://host.docker.internal:8080/catalog/category/'+str(producto['category'])+'/', headers=header_m4)
    datos={
        "product":producto,
        "category":categoria.json(),
        "sum_cart":suma_carrito,
        "quantity_cart":cantidad
    }
    return render_template("/products/detail.html", result=datos)

@app.route("/orders/search/", methods=['GET', 'POST'])
def search():
    carrito=requests.get('http://host.docker.internal:8080/catalog/cart/', headers=header_m4)
    json_carrito=carrito.json()
    suma_carrito=0.0
    cantidad=0
    for product in json_carrito:
        suma_carrito+=float(product['total_product'])
        cantidad+=1
    data={
        "sum_cart":suma_carrito,
        "quantity_cart":cantidad
    }
    if request.method == "POST":
        order_id=request.form['order_id']
        data={
            "order_id":order_id
        }
        orden = requests.post('http://host.docker.internal:8080/orders/order/get/', headers=header_m5, data=data)
        json_orden=orden.json()
        data={
                "sum_cart":suma_carrito,
                "quantity_cart":cantidad
            }
        if str(orden.status_code)=="403":
            data={
                "sum_cart":suma_carrito,
                "quantity_cart":cantidad,
                "mensaje":"Tiempo de cancelación excedido."
            }
            return render_template("orders/order_form.html", result=data)
        if str(orden.status_code)=="404":
            data={
                "sum_cart":suma_carrito,
                "quantity_cart":cantidad,
                "mensaje":"Orden no encontrada."
            }
            return render_template("orders/order_form.html", result=data)
        sum=0.0
        for product in json_orden:
            sum+=float(product['total_item_price'])
        data={
            "json":json_orden,
            "total":sum,
            "sum_cart":suma_carrito,
            "quantity_cart":cantidad,
            "order_id":order_id
        }
        return render_template('orders/orders.html', result=data)
    else:
        return render_template("/orders/order_form.html", result=data)

@app.route("/orders/create/", methods=['GET', 'POST'])
def create():
    carrito=requests.get('http://host.docker.internal:8080/catalog/cart/', headers=header_m4)
    json_carrito=carrito.json()
    suma_carrito=0.0
    cantidad=0
    for product in json_carrito:
        suma_carrito+=float(product['total_product'])
        cantidad+=1
    data={
        "cart":json_carrito,
        "sum_cart":suma_carrito,
        "quantity_cart":cantidad
    }
    if request.method == "POST":
        info={
            'first_name':request.form['first_name'],
            'last_name':request.form['last_name'],
            'email':request.form['email'],
            'address':request.form['address'],
            'postal_code':request.form['postal_code'],
            'city':request.form['city']
        }
        order=requests.post('http://host.docker.internal:8080/orders/order/create/order/', headers=header_m5, data=info)
        order_json=order.json()
        for item in json_carrito:
            data={
                "order":order_json['id'],
                "name":item['product']['name'],
                "image":item['product']['image'],
                "price":item['product']['price'],
                "quantity":item['quantity'],
                "total_product":item['total_product']
            }
            order = requests.post('http://host.docker.internal:8080/orders/order/create/order-item/', headers=header_m5, data=data)

        data_mail = {
            "order_id":order_json['id']
        }
        
        correo = requests.post('http://host.docker.internal:8080/orders/order/send-mail/',headers= header_m5, data=data_mail )
        carrito=requests.get('http://host.docker.internal:8080/catalog/cart/', headers=header_m4)
        data={
            "order":order_json,
            "cart":json_carrito,
            "sum_cart":suma_carrito,
            "quantity_cart":0
        }
        requests.delete("http://host.docker.internal:8080/catalog/cart/clear", headers=header_m4)
        return render_template('/orders/created.html', result=data)
    else:
        return render_template("/cart/create.html", result=data)
        
        
@app.route("/orders/cancel/<id>",methods=['GET']) 
def cancel_order(id):
    json = {
        "order_id":id,
    }
    carrito=requests.delete('http://host.docker.internal:8080/orders/order/modify/', headers=header_m5, data=json)
    return redirect(url_for("list"))

@app.route("/orders/cancel/",methods=['POST']) 
def cancel_order_item():
    
    items_json = {}
    items=request.form.getlist("items")
    for i in range(len(items)):
        items_json[i] = items[i]
    

    respuesta=requests.put('http://host.docker.internal:8080/orders/order/modify/', headers=header_m5, data=items_json)
    return redirect(url_for("list"))


@app.route("/cart/", methods=['GET', 'POST'])
def cart():
    carrito=requests.get('http://host.docker.internal:8080/catalog/cart/', headers=header_m4)
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
    return render_template("/cart/detail.html", result=data)


@app.route("/cart/remove/", methods=['POST'])
def cart_delete():
    product_id = request.form['product_id']
    data = {
        "product_id":product_id
    }
    carrito_remove = requests.delete('http://host.docker.internal:8080/catalog/cart/', headers=header_m4, data=data)
    carrito=requests.get('http://host.docker.internal:8080/catalog/cart/', headers=header_m4)
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
    return render_template("/cart/detail.html", result=data_env)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')