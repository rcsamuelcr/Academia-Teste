from django.db import models

# Create your models here.

class Alunos(models.Model):

    name = models.CharField(max_length=50)
    nascimento = models.DateField()
    telefone = models.FloatField()
    email = models.EmailField()
    rg = models.FloatField(max_length=11)
    cpf = models.FloatField()
    bairro = models.CharField(max_length=40)
    rua = models.CharField(max_length=80)
    numero = models.FloatField()
    inscricao = models.DateField()

    def __str__(self):
        return self.name