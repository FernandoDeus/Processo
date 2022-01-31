from django.db import models

# Criei a classe que cria a tabela no banco de dados
class cadastro(models.Model):
    nome_projeto = models.CharField(max_length=150)
    data_inicio = models.IntegerField()
    data_termino = models.IntegerField()
    valor_projeto = models.DecimalField(max_digits=8, decimal_places=2)
    risco = models.CharField(max_length=100)
    participantes = models.CharField(max_length=150)


