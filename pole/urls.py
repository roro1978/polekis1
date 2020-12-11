from django.urls import path
from.views import pole, contacto, quienessomos, galeria

urlpatterns = [
    path('', pole,name='index'),
    path('contacto/', contacto, name='contacto'),
    path('galeria/', galeria, name='galeria'),
    path('quienessomos/', quienessomos, name='quienessomos' ),
]
