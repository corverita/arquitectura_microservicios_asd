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

from .serializers import CarritoItemSerializer, ProductSerializer
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

    # def product_list(self, request, category_slug=None):
    #     category = None

    #     # Se obtienen todas las categorías.
    #     categories = Category.objects.all()

    #     # Se filtran los productos que se encuentran disponibles.
    #     products = Product.objects.filter(available=True)

    #     # Si se recibió el slug de la categoría, se seleccionan solo los productos pertenecientes
    #     # a esa categoría, de forma contraria, se envían todos los productos para mostrarlos.
    #     if category_slug:
    #         category = get_object_or_404(Category, slug=category_slug)
    #         products = products.filter(category=category)
        
    #     return render(request, 'shop/product/list.html', {'category': category,
    #                                                     'categories': categories,
    #                                                     'products': products})


    # def product_detail(self, request, id, slug):

    #     # Se obtiene la información del producto que se mostrará.
    #     product = get_object_or_404(Product, id=id, slug=slug, available=True)

    #     # Se obtiene el formulario para agregar elementos de este producto al carrito.
    #     cart_product_form = CartAddProductForm()
    #     return render(request,
    #                 'shop/product/detail.html',
    #                 {'product': product,
    #                 'cart_product_form': cart_product_form})

class CarritoItemViewSet(viewsets.ViewSet):

    def add(self,request):
        body=request.body
        product_id=body['product_id']
        product=get_object_or_404(Product,id=product_id)
        quantity=body['quantity']
        quantity=int(quantity)
        total=int(product.price)*int(quantity)
        
        carrito=CarritoItem(quantity=quantity,product=product,total_product=total)

        for item in CarritoItem.objects.all():
            if item.product==product:
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