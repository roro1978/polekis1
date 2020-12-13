from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Marca(models.Model):
  nombre = models.CharField(max_length=50)

  def __str__(self):
    return self.nombre

class Producto(models.Model):
  publicador = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  nombre = models.CharField(max_length=50)
  precio = models.IntegerField()
  descripcion = models.TextField()
  nuevo = models.BooleanField()
  marca = models.ForeignKey('pole.Marca',on_delete=models.CASCADE)
  
  def publish(self):
    self.fecha = timezone.now()

  def __str__(self):
    return self.nombre