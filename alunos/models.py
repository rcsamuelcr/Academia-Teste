from django.db import models

# Create your models here.

class Alunos(models.Model):

    inscricao = models.DateField(primary_key=True)
    name = models.CharField(max_length=50)
    # sexo
    nascimento = models.DateField()
    telefone = models.FloatField()
    email = models.EmailField()
    rg = models.FloatField(max_length=11)
    cpf = models.FloatField()
    bairro = models.CharField(max_length=40)
    rua = models.CharField(max_length=80)
    numero = models.FloatField()

    def __str__(self):
        return self.name
        
class DadosAcademia(models.Model):
    dat_medidas = models.DateField()
    altura = models.FloatField()
    peso = models.FloatField()
    imc = models.FloatField()
    gordura = models.FloatField()
    liquido = models.FloatField()
    pa = models.FloatField()
    pulso = models.FloatField()
    bat_cardiaco = models.FloatField()
    quadriceps = models.FloatField()
    torax = models.FloatField()
    cintura = models.FloatField()
    culote = models.FloatField()
    biceps_D = models.FloatField()
    biceps_E = models.FloatField()
    coxa_D = models.FloatField()
    coxa_E = models.FloatField()