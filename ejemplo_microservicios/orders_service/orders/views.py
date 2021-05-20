from .serializers import OrderItemSerializer, OrderSerializer
from .models import Order,OrderItem
from django.shortcuts import redirect, render
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets,status
import json
from django.core.mail import send_mail
from datetime import datetime, timedelta
from django.utils import timezone

# Create your views here.

class Orders_ViewSet(viewsets.ViewSet):
    # Envia un email como si fuera un recibo de orden.
    def send_email(self,change, action, order_id,items=None):
        order = Order.objects.get(id=order_id)
        if items==None:
            items = OrderItem.objects.filter(order=order)
        subject = 'Order nr. {}'.format(order.id)
        # Se define el mensaje a enviar.
        message = 'Dear {},\n\nYou have successfully {} your order. Your order id is {}.\n\n\n'.format(order.first_name,change,order_id)
        message_part2 = 'Your {}: \n\n'.format(action)
        mesagges = []

        for item in items:
            msg = str(item.quantity) + 'x '+ str(item.product_name) +'  $'+ str(item.total_item_price)+ '\n'
            mesagges.append(msg)

        message_part3 = ' '.join(mesagges)
        body = message + message_part2 + message_part3

        # Se envía el correo.
        send_mail(subject, body, 'oscarcorverita@gmail.com', [order.email], fail_silently=False)
        
    def send_correo(self,order_id):
        # Se obtiene la información de la orden.
        order = Order.objects.get(id=order_id)
        cart = OrderItem.objects.filter(order=order)

        # Se crea el subject del correo.
        subject = 'Order nr. {}'.format(order.id)

        # Se define el mensaje a enviar.
        message = 'Dear {},\n\nYou have successfully placed an order. Your order id is {}.\n\n\n'.format(order.first_name,order.id)
        message_part2 = 'Your order: \n\n'
        mesagges = []
        total_price = 0.0
        for item in cart:
            total_price += int(item.total_item_price)
            msg = str(item.quantity) + 'x '+ str(item.product_name) +'  $'+ str(item.total_item_price)+ '\n'
            mesagges.append(msg)
            
        
        message_part3 = ' '.join(mesagges)
        message_part4 = '\n\n\n Total: $'+ str(total_price)
        body = message + message_part2 + message_part3 + message_part4

        # Se envía el correo.
        send_mail(subject, body, 'oscarcorverita@gmail.com', [order.email], fail_silently=False)

    def create_order(self,request):
        #informacion=request.data.get("informacion")
        order = Order(first_name=request.data['first_name'],
            last_name= request.data['last_name'],
            email= request.data['email'],
            address=request.data['address'],
            city=request.data['city'],
            postal_code=request.data['postal_code']
        )
        order.save()
        serializer=OrderSerializer(order)

        return Response(serializer.data)

    def create_order_item(self,request):
        order=Order.objects.last()
        orderI= OrderItem(order=order,
                        product_name=request.data['name'],
                        image=request.data['image'],
                        price=request.data['price'],
                        quantity= request.data['quantity'],
                        total_item_price=float(request.data['total_product']))
        orderI.save()
        return Response(status=status.HTTP_201_CREATED)
    
    def enviar_correo(self,request):
        order_id=request.data['order_id']
        order=get_object_or_404(Order,id=order_id)
        self.send_correo(order.id)
        return Response(status=status.HTTP_200_OK)
    
    def destroy(self,request):
        order_id=request.data['order_id']
        order=get_object_or_404(Order,id=order_id) #Se obtiene la orden
        self.send_email('cancelled','cancelation',order.id)
        order.delete()
        return Response(status=status.HTTP_200_OK)
    
    def search(self,request):
        order_id=request.POST.get('order_id')
        order=get_object_or_404(Order,id=order_id) #Se obtiene la orden
        if self.verify_expired_time(order_id):
            order_items=OrderItem.objects.filter(order=order) #Se obtienen los articulos
            ois = OrderItemSerializer(order_items, many=True)
            return Response(ois.data)
        else:
            return Response(status= status.HTTP_403_FORBIDDEN)
    
    def update(self,request):
        
        items_deleted=[]

        for i, value in request.data.items():
            orderI= OrderItem.objects.get(id=value)
            items_deleted.append(orderI)
            orderI.delete()
        
        order = Order.objects.get(id= items_deleted[0].order.id)
        order_id=order.id
        items_restantes = OrderItem.objects.filter(order=order)
        ##Enviar correo de actualización
        if len(items_restantes)>0:
            self.send_email('partially cancelled','cancelation',order_id, items_deleted)
            self.send_email('updated', 'order',order_id, items_restantes)
        else:
            self.send_email('cancelled','cancelation',order_id,items_deleted)
            order.delete()
        
        return Response(status = status.HTTP_200_OK)

    def verify_expired_time(self,id):
        order=Order.objects.get(id=id)
        hora=timezone.now()
        offset=hora-order.created
        horas_diferencia=offset.days*24+(offset.seconds/3600)
        if(horas_diferencia<24):
            return True
        else:
            return False
    
    
    
        