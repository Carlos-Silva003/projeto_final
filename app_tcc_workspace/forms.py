from django import forms
from .models import TCC

class TCForm(forms.ModelForm):
    class Meta:
        model = TCC
        fields = ['titulo', 'capa', 'descricao', 'curso', 'data_entrega', 'status', 'data_inicio', 'autores']
