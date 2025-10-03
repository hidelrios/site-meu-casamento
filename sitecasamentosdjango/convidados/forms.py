from django import forms
from .models import Convidado

class ConvidadoForm(forms.ModelForm):
    class Meta:
        model = Convidado
        fields = ["nome", "contato"]
