"""
URL configuration for tutorial1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
#Agregar el import de include
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Para dividir las urls, se crea un archivo urls dentro de cada app, y desde aca se lo vincula
    # El resto de las urls de la app hola van dentro de hola.urls
    path("hola/",include("hola.urls")),
    path("tareas/",include("listaTareas.urls")),
]
