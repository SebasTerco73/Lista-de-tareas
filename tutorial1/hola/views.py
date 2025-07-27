from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Ruta principal, con html
def hola(request):
    return render(request, 'hola/index.html')

# Ruta secundaria sin html, solo mensaje
def vader(request):
    return HttpResponse("Hola Darth Vader")

# Ruta nombre sin html
def saludar(request, nombre):
    return HttpResponse(f"Hola señor {nombre}")

# Ruta nombre con html
def saludarHtml(request,nombre):
    context = {'nombre':nombre}
    return render(request, 'hola/index.html', context)

def moneda(request):
    num = 1
    context = {"num" : num}
    return render(request, 'hola/moneda.html', context)