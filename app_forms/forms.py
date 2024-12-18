from django import forms
from .models import TCC

class TCCForm(forms.ModelForm):
    class Meta:
        model = TCC
        fields = [
            'titulo',
            'capa',
            'descricao',
            'autores',
            'data_entrega',
            'curso',
            'data_inicio'
        ]
