#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: models.py
#
# Descripción:
#
#   En este archivo se definen los modelos para la app del Catálogo
#
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |                         |                        |
#           |                       |  - Representa la        |  - Se indica los       |
#           |                       |    orden que se crea    |    campos del modelo   |
#           |         Order         |    con los datos del    |    así como sus pro-   |
#           |                       |    cliente para fina-   |    piedades.           |
#           |                       |    lizar la compra.     |                        |
#           |                       |                         |                        |
#           +-----------------------+-------------------------+------------------------+
#           |                       |                         |                        |
#           |                       |  - Representa cada uno  |  - Se indica los       |
#           |                       |    de los items de la   |    campos del modelo   |
#           |       OrderItem       |    orden, los cuales    |    así como sus pro-   |
#           |                       |    vienen de los items  |    piedades.           |
#           |                       |    del carrito.         |                        |
#           |                       |                         |                        |
#           +-----------------------+-------------------------+------------------------+
#
#-------------------------------------------------------------------------

from django.db import models

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    # Método to String de la clase, la cual es representada por el campo 'id'.
    def __str__(self):
        return 'Order {}'.format(self.id)

    # Método que obtiene el costo total de la orden.
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100, null=True)
    image=models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    total_item_price=models.DecimalField(max_digits=11, decimal_places=2, null=True)

    # Método to String de la clase, la cual es representada por el campo 'id'.
    def __str__(self):
        return '{}'.format(self.id)

    # Método que obtiene el costo total del item de la orden.
    def get_cost(self):
        return self.price * self.quantity