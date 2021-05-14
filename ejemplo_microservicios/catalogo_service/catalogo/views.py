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

from .serializers import ProductSerializer
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from .models import Category, Product
from rest_framework import viewsets,status

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
