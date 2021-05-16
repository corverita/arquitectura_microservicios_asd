from django.urls import path
from .views import *

app_name='cart'

urlpatterns = [
    path('product/',CarritoItemViewSet.as_view({
        "get":'list',
        'post':'add',
        'delete':'remove_all',
        'put':'remove_item'
    }), name="product")
]
    