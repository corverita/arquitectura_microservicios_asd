#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------------------------
# Archivo: views.py
#
# Descripción:
#   En este archivo se definen las vistas para la app del catálogo del sistema.
#
#   A continuación se describen los métodos que se implementaron en este archivo:
#
#                                               Métodos:
#           +------------------------+--------------------------+-----------------------+
#           |         Nombre         |        Parámetros        |        Función        |
#           +------------------------+--------------------------+-----------------------+
#           |                        |  - request: datos de     |  - Obtiene los datos  |
#           |                        |    la solicitud.         |    para mostrar la    |
#           |    product_list()      |                          |    lista de los pro-  |
#           |                        |  - category_slug: slug   |    ductos de la cate- |
#           |                        |    de la categoría.      |    goría indicada.    |
#           +------------------------+--------------------------+-----------------------+
#           |                        |  - request: datos de     |                       |
#           |                        |    la solicitud.         |  - Obtiene los datos  |
#           |    product_detail()    |                          |    para mostrar el    |
#           |                        |  - id: id del producto.  |    detalle del pro-   |
#           |                        |                          |    ducto indicado.    |
#           |                        |  - slug: slug del pro-   |                       |
#           |                        |    ducto a mostrar.      |                       |
#           +------------------------+--------------------------+-----------------------+
#
#--------------------------------------------------------------------------------------------------

from .serializers import CarritoItemSerializer, ProductSerializer, CategorySerializer
from django.shortcuts import redirect, render, get_object_or_404
from rest_framework.response import Response
from .models import CarritoItem, Category, Product
from rest_framework import viewsets,status
import json

class CatalogViewSet(viewsets.ViewSet):

    # Método que se accede por la URL /django
    def list(self, request):
        # Se obtiene la lista de productos
        products = Product.objects.all()
        print(products)
        # Se crea el serializer y se envía como response
        serializer_product = ProductSerializer(products, many=True)
        return Response(serializer_product.data)

    def product_detail(self,request,pk):
        product=Product.objects.get(id=pk)
        serializer_product=ProductSerializer(product,many=False)
        return Response(serializer_product.data)

class CarritoItemViewSet(viewsets.ViewSet):

    def clear(self, request):
        CarritoItem.objects.all().delete()
        return Response(status=status.HTTP_200_OK)

    def add(self,request):
        product_id=request.data['product_id']
        product=get_object_or_404(Product,id=product_id)
        quantity=int(request.data['quantity'])
        quantity=int(quantity)
        total=int(product.price)*int(quantity)

        carrito = CarritoItem(quantity=quantity, product=product, total_product=total)

        for item in CarritoItem.objects.all():
            print(item.product)
            print(product)
            if item.product == product:
                item.quantity += quantity
                item.total_product = product.price*item.quantity
                product.stock -= quantity
                product.save()
                item.save()
                return redirect("cart:product")
        product.stock -= quantity
        product.save()
        carrito.save()
        return redirect("cart:product")

    def remove_item(self,request):
        product_id=request.data.get('product_id')
        product=Product.objects.get(name=product_id)
        carrito_item=get_object_or_404(CarritoItem,product=product)
        product.stock+=carrito_item.quantity
        product.save()
        carrito_item.delete()
        return redirect("cart:product")

    def remove_all(self,request):
        carrito_items=CarritoItem.objects.all().delete()
        return redirect("cart:product")

    # Método que se accede por la URL /django
    def list(self, request):
        # Se obtiene la lista de productos
        carrito = CarritoItem.objects.all()
        print(carrito)
        # Se crea el serializer y se envía como response
        serializer_cart = CarritoItemSerializer(carrito, many=True)
        return Response(serializer_cart.data)


class CategoriaViewSet(viewsets.ViewSet):

    def list(self, request):
        # Se obtiene la lista de productos
        categoria = Category.objects.all()
        # Se crea el serializer y se envía como response
        serializer_product = CategorySerializer(categoria, many=True)
        return Response(serializer_product.data)

    def get(self, request, id):
        categoria=get_object_or_404(Category,id=id)
        serializer=CategorySerializer(categoria)
        return Response(serializer.data)
    
class ProductCategoryViewSet(viewsets.ViewSet):
    def list(self, request,id):
        categoria=get_object_or_404(Category, id=id)
        products=Product.objects.filter(category=categoria)
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data)

