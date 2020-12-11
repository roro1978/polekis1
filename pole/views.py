from django.shortcuts import render

# Create your views here.

def pole(request):
    return render(request, 'pole/index.html')

def contacto(request):
    return render(request, 'pole/contacto.html') 

def quienessomos(request):
    return render(request, 'pole/quienessomos.html')

def galeria(request):
    return render(request, 'pole/galeria.html')    