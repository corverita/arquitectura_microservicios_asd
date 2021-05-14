from django.urls import path

from .views import *

urlpatterns = [
    path('cancel/', Orders_ViewSet.as_view({
        'post': 'create', #create
        'delete':'destroy', #cancel order
        'put':'update' #update order
    })),
    path('search/<int:id>', Orders_ViewSet.as_view({
        'get':'search'
    })),
]