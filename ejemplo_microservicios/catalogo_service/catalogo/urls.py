from django.urls import path
from .views import *

app_name='cart'

urlpatterns = [
    path('cart/',CarritoItemViewSet.as_view({
        "get":'list',
        'post':'add',
        'delete':'remove_item'
    }), name="product"),
    path('cart/clear/', CarritoItemViewSet.as_view({
        'delete': 'clear',
    })),
    path('product', CatalogViewSet.as_view({
        'get': 'list',
    })),
    path('product/<int:pk>/', CatalogViewSet.as_view({
        'get': 'product_detail',
    })),
    path('categories/', CategoriaViewSet.as_view({
        'get': 'list'
    })),
    path('category/<int:id>/',CategoriaViewSet.as_view({
        'get':'get'
    })),
    path('product/category/<int:id>/',ProductCategoryViewSet.as_view({
        'get':'list'
    })),
    
]
    