from rest_framework import serializers
from .models import CarritoItem, Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class CarritoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CarritoItem
        fields='__all__'
        depth=1