from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets,status

# Create your views here.

class Orders_ViewSet(viewsets.ViewSet):
    def saluda(self,request):
        json = {'saludo':"HOlA"}
        return Response(json)
    

    def create(self, request):
        pass
    
    def destroy(self,request):
        pass
    
    def search(self,request):
        pass
    
    def update(self,request):