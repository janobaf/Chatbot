from django import forms
from .models import Respuestas


class RegistroFormulario(forms.ModelForm):
    class Meta:
        model = Respuestas
        fields=(
                'respuesta',
                'imagen',
                'musica')