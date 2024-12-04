from django import forms
from .models import Visita

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = '__all__'  # O puedes especificar los campos que quieres incluir en el formulario manualmente