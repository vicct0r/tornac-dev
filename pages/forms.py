from django import forms
from .models import Aplicativo


class AplicativoModelForm(forms.ModelForm):
    class Meta:
        model = Aplicativo
        fields = ['ativo', 'titulo', 'status', 'descricao', 'imagem', 'url', 'tags', 'categoria']