from django.urls import path
from .views import *

urlpatterns = [
    path('product', CatalogViewSet.as_view({
        'get': 'list',
    })),
    path('product/<int:pk>/', CatalogViewSet.as_view({
        'get': 'product_detail',
    })),
]