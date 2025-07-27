from django import forms

#Crea un formulario de django
class AgregarTarea(forms.Form):
    # El nombre de esta variable aparece en el html
    # Usar como llave para acceder a este campo, en views.py
    #Campo obligatorio por defecto
    tarea = forms.CharField()