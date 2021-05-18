from django.urls import path
from .views import *

app_name='cart'

urlpatterns = [
    path('product/cart/',CarritoItemViewSet.as_view({
        "get":'list',
        'post':'add',
        'delete':'remove_item'
    }), name="product"),
    path('product', CatalogViewSet.as_view({
        'get': 'list',
    })),
    path('product/<int:pk>/', CatalogViewSet.as_view({
        'get': 'product_detail',
    })),
    path('product/category/', CategoriaViewSet.as_view({
        'get': 'list',
    })),
    path('product/category/<int:id>/',ProductCategoryViewSet.as_view({
        'get':'list'
    }))
]
    