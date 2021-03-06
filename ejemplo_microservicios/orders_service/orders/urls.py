from django.urls import path

from .views import *

urlpatterns = [
    path('modify/', Orders_ViewSet.as_view({
        'delete':'destroy', #cancel order
        'put':'update' #update order
    })),
    path('get/', Orders_ViewSet.as_view({
        'post':'search'
    })),
    path("create/order/",Orders_ViewSet.as_view({
        'post':'create_order'
    })),
    path("create/order-item/",Orders_ViewSet.as_view({
        'post':'create_order_item'
    })),
    path("send-mail/",Orders_ViewSet.as_view({
        'post':'enviar_correo'
    })),
]