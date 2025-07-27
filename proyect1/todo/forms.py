from django import forms
from .models import Tarea


# ModelForm -> Django nos permite asociar el formulario a un modelo
class TareaForm(forms.ModelForm):

    # La clase meta le dice a la clase TareaForm como comportarse
    class Meta:
        # Datos de la clase tarea en models
        model = Tarea
        fields = ["tarea"]
        widgets = {
            "tarea": forms.TextInput(attrs={
                "style": "width: 300px;"  # Ajustá este valor a gusto
            })
        }
    
