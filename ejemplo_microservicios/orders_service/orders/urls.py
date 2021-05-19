from django.urls import path

from .views import *

urlpatterns = [
    path('a/', Orders_ViewSet.as_view({
        'post': 'create', #create
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
]