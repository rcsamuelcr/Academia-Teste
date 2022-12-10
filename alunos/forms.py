from django import forms
from .models import Alunos

class AlunosModelForm(forms.ModelForm):
    class Meta:
        model = Alunos
        fields = ['name', 'nascimento', 'telefone', 'email', 'rg', 'cpf', 'bairro', 'rua', 'numero', 'inscricao']
        