from .models import Order,OrderItem
from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets,status
import json

# Create your views here.

class Orders_ViewSet(viewsets.ViewSet):

    def create(self, request):
        body=json.loads(request.body)
        #Obtener y rellenar los datos del usuario en una Order
        informacion=body[0]
        print(informacion['first_name'])
        order=Order(first_name=informacion['first_name'],
            last_name=informacion['last_name'],
            email=informacion['email']
            ,address=informacion['address'],
            city=informacion['city'],
            postal_code=informacion['postal_code'])
        order.save()
        
        #Relleno
        products=body[1] #tambien podríamos ponerle un nombre especifico al diccionario
        
        #Obtener los items del carrito y rellenar uno o varios OrderItem
        for product in products:
            print(product)
            print(product['product']['id'])
            orderI= OrderItem(order=order,product = product['product']['id'],price=product['product']['price'],quantity= product['quantity'])
            orderI.save()
        pass

    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # email = models.EmailField()
    # address = models.CharField(max_length=100)
    # postal_code = models.CharField(max_length=20)
    # city = models.CharField(max_length=100)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    # paid = models.BooleanField(default=False)
    
    # order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    # product = models.IntegerField()
    # price = models.DecimalField(max_digits=11, decimal_places=2)
    # quantity = models.PositiveIntegerField(default=1)
    
    # [
    #     {
    #         "first_name":"Oscar",
    #         "last_name": "Rios",
    #         "email": "oscar@gmail.com",
    #         "address":"Zacatecas",
    #         "postal_code":"98053",
    #         "city":"zacatecas"
    #     },
    #     {
    #         "id": 6,
    #         "quantity": 1,
    #         "total_product": "114.00",
    #         "product": {
    #             "id": 2,
    #             "name": "Microsoft 3RA-00022 Surface Ergonomic Keyboard",
    #             "slug": "microsoft_3RA_00022_ergonomic_keyboard",
    #             "image": "/img/teclado_2.jpg",
    #             "description": "Compatible with Surface Pro 4, Surface Book, Surface Studio, natural arc and slope, double-cushioned palm rest covered in stunning Alcantara. The Surface Ergonomic Keyboardâ€™s double-cushioned palm rest uses a special, ultra-durable version of Alcantara - a unique, proprietary material, sourced only in Italy, with aesthetic, sensory, and technical qualities unlike anything youâ€™ve ever experienced.",
    #             "price": "114.95",
    #             "stock": 13,
    #             "available": true,
    #             "created": "2021-02-21T00:00:00Z",
    #             "updated": "2021-05-16T01:00:49.380594Z",
    #             "category": 1
    #         }
    #     }
    # ]
    
    def destroy(self,request):
        pass
    
    def search(self,request):
        body=json.loads(request.body)
        print(body)
        pass
    
    def update(self,request):
        pass