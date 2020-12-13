from rest_framework import serializers
from .models import Producto, Marca
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class ProductoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Producto
        fields = ['publicador','nombre', 'precio', 'marca', 'descripcion', 'nuevo' ]

class MarcaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Marca
        fields = ['nombre']