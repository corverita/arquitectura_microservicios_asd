from django.urls import path

from .views import *

urlpatterns = [
    path('', Orders_ViewSet.as_view({
        'post': 'create', #create
        'delete':'destroy', #cancel order
        'put':'update' #update order
    })),
    path('get/', Orders_ViewSet.as_view({
        'post':'search'
    })),
]