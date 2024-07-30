from django import forms
from .models import Renda, Despesa

class RendaForm(forms.ModelForm):
    class Meta:
        model = Renda
        fields = ['valor', 'data', 'descricao']


class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['categoria', 'valor', 'data', 'descricao']