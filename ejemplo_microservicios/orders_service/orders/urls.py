from django.urls import path

from .views import *

urlpatterns = [
    path('', Orders_ViewSet.as_view({
        'get':'search',
        'post': 'create', #create
        'delete':'destroy', #cancel order
        'put':'update' #update order
    })),
]