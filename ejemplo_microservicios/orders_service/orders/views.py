from .serializers import OrderItemSerializer
from .models import Order,OrderItem
from django.shortcuts import redirect, render
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
        order=Order(first_name=informacion['first_name'],
            last_name=informacion['last_name'],
            email=informacion['email'],
            address=informacion['address'],
            city=informacion['city'],
            postal_code=informacion['postal_code'])
        order.save()
        
        #Relleno
        products=body[1] #tambien podríamos ponerle un nombre especifico al diccionario
        
        #Obtener los items del carrito y rellenar uno o varios OrderItem
        print(products)
        for product in products:
            orderI= OrderItem(order=order,
                        product_name=product['product']['name'],
                        image=product['product']['image'],
                        price=product['product']['price'],
                        quantity= product['quantity'],
                        total_item_price=float(product['total_product'])*float(product['quantity']))
            orderI.save()
        return Response(status=status.HTTP_201_CREATED)

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
        body=json.loads(request.body)
        order_id=body['order_id']
        order=get_object_or_404(Order,id=order_id) #Se obtiene la orden
        order.delete()
        return Response(status=status.HTTP_200_OK)
    
    def search(self,request):
        order_id=request.POST.get('order_id')
        order=get_object_or_404(Order,id=order_id) #Se obtiene la orden
        order_items=OrderItem.objects.filter(order=order) #Se obtienen los articulos
        ois = OrderItemSerializer(order_items, many=True)
        return Response(ois.data)
    
    def update(self,request):
        body = json.loads(request.body)
        orderId = body[0]
        for pos in body[0]:
            orderItemId = body[0][pos]
            orderItem = get_object_or_404(OrderItem,id=orderItemId);
            orderItem.delete()
            
        return Response(status = status.HTTP_200_OK)