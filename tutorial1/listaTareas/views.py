from django.shortcuts import render, redirect
from .forms import AgregarTarea


tareas = ["Aprender Django", "Inscripcion materias"]

# Create your views here.
def home(request):
    context = {"tareas":tareas}
    return render(request, "listaTareas/home.html", context)

def add(request):
    # Si el metodo es post (el usuario envia informacion)
    if request.method == "POST":
        # crea el form con los datos enviados por el user
        form = AgregarTarea(request.POST)
        # Validacion de django, que no este vacio y que cumpla las reglas del form
        if form.is_valid():
            # Acceder al valor validado y limpio. Nombre de la variable en el metodo AgregarTarea
            tarea = form.cleaned_data["tarea"]
            tareas.append(tarea)
            #Al finalizar redirecciona a la pag principal
            return redirect('home')
    else: # Get (cuando el usuario visita la pagina)
        #Se muestra el form vacio
        form = AgregarTarea()

    context = {"form":form}
    return render(request, "listaTareas/add.html",context)
