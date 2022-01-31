from django.forms import ModelForm
from sistema.models import cadastro

# Aqui criei a classe que faz a conexão banco de dados e o formulário
class cadastroform(ModelForm):
    class Meta:
        model = cadastro
        fields = ['nome_projeto', 'data_inicio', 'data_termino', 'valor_projeto', 'risco', 'participantes']
