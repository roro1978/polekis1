from django.urls import path
from.views import index, contacto, quienessomos, galeria

urlpatterns = [
    path('', index, name="home"),
    path('contacto/', contacto, name='contacto'),
    path('quienessomos/', quienessomos, name='quienessomos'),
    path('galeria/', galeria, name='galeria'),
]
