from django.db import models

# Create your models here.

class Alunos(models.Model):

    inscricao = models.DateField(auto_now = True,primary_key=True)
    nome = models.CharField(max_length=50)
    # sexo
    nascimento = models.DateField()
    telefone = models.FloatField()
    email = models.EmailField()
    rg = models.FloatField(max_length=11)
    cpf = models.FloatField()
    bairro = models.CharField(max_length=40)
    rua = models.CharField(max_length=80)
    num_residencia = models.FloatField()

    def __str__(self):
        return self.nome

class DadosAcademia(models.Model):
    dat_medidas = models.DateField(primary_key=True)
    aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE)
    altura = models.FloatField(blank =True, null= True)
    peso = models.FloatField(blank =True, null= True)
    imc = models.FloatField(blank =True, null= True)
    gordura = models.FloatField(blank =True, null= True)
    liquido = models.FloatField(blank =True, null= True)
    pa = models.FloatField(blank =True, null= True)
    pulso = models.FloatField(blank =True, null= True)
    bat_cardiaco = models.FloatField(blank =True, null= True)
    quadriceps = models.FloatField(blank =True, null= True)
    torax = models.FloatField(blank =True, null= True)
    cintura = models.FloatField(blank =True, null= True)
    culote = models.FloatField(blank =True, null= True)
    biceps_D = models.FloatField(blank =True, null= True)
    biceps_E = models.FloatField(blank =True, null= True)
    coxa_D = models.FloatField(blank =True, null= True)
    coxa_E = models.FloatField(blank =True, null= True)