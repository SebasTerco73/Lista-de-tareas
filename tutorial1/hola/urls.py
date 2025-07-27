#Crear este archivo
from django.urls import path
# Importar del directorio actual (.)
from . import views

urlpatterns = [
    path('', views.hola, name='hola'),
    # path('vader/', views.vader, name="vader"),
    # path('<str:nombre>/', views.saludar, name="saludo"),
    # path('<str:nombre>/', views.saludarHtml, name="saludo"),
    path('moneda', views.moneda, name="moneda"),
]