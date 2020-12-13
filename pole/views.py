#rest_framework
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductoSerializer, MarcaSerializer, UserSerializer
from .models import Producto, Marca
from django.contrib.auth.models import User
# Create your views here.

def pole(request):
    return render(request, 'pole/index.html')

def contacto(request):
    return render(request, 'pole/contacto.html') 

def quienessomos(request):
    return render(request, 'pole/quienessomos.html')

def galeria(request):
    return render(request, 'pole/galeria.html')

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer