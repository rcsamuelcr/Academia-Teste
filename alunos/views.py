from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.decorators import login_required
from .models import Alunos
# Create your views here.

# @login_required(login_url='login')  ------------------------------- DANDO ERRO AO ADICIONAR ESTÁ LINHA ----------------------------------


def alunos(request):
    return render(request, 'template_alunos/alunos.html')

def cad_alunos(request):
    if request.method == "POST":

        inscricao = request.POST.get('inscricao')
        nome = request.POST.get('nome')
        # sexo
        nascimento = request.POST.get('nascimento')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        rg = request.POST.get('rg')
        cpf = request.POST.get('cpf')
        bairro = request.POST.get('bairro')
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')

        dat_medidas = request.POST.get('dat_medidas')
        # Objetivo
        # Status da matricula
        altura = request.POST.get('altura')
        peso = request.POST.get('peso')
        imc = request.POST.get('imc')
        gordura = request.POST.get('gordura')
        liquido = request.POST.get('liquido')
        pa = request.POST.get('pa')
        pulso = request.POST.get('pulso')
        bat_cardiaco = request.POST.get('bat_cardiaco')
        quadriceps = request.POST.get('quadriceps')
        torax = request.POST.get('torax')
        cintura = request.POST.get('cintura')
        culote = request.POST.get('culote')
        biceps_D = request.POST.get('biceps_D')
        biceps_E = request.POST.get('biceps_E')
        coxa_D = request.POST.get('coxa_D')
        coxa_E = request.POST.get('coxa_E')

        if not nome or not nascimento or not telefone \
                or not email or not rg or not cpf or not bairro\
                or not rua or not numero or not inscricao:
            messages.error(request, "Não pode deixar campos da área de dados pessoais em branco!")
            return render(request, 'template_alunos/cad_alunos.html')
        try:
            validate_email(email)
        except:
            messages.info(request, "E-mail inválido!")
            return render(request, 'template_alunos/cad_alunos.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email já existente!")
            return render(request, 'template_alunos/cad_alunos.html')

        messages.success(request, "Registrado com sucesso!")

        Alunos.objects.create(inscricao ='inscricao', nome='nome', nascimento='nascimento', telefone='telefone' , email='email',
                                        rg='rg', cpf='cpf', bairro='bairro', rua='rua', num_residencia='numero')


        DadosAcademia.objects.create(dat_medidas='dat_medidas', altura ='altura', peso = 'peso', imc = 'imc', gordura = 'gordura',
                                    liquido = 'liquido', pa = 'pa', pulso = 'pulso', bat_cardiaco = 'bat_cardiaco', quadriceps = 'quadriceps',
                                    torax = 'torax', cintura = 'cintura', culote = 'culote', biceps_D = 'biceps_D', biceps_E = 'biceps_E',
                                    coxa_D = 'coxa_D', coxa_E = 'coxa_E')

        Alunos.save()
        DadosAcademia.save()

        return redirect('alunos')

    return render(request, 'template_alunos/cad_alunos.html')


@login_required(login_url='login')
def edit_cad_aluno(request):
    if request.method == "POST":
        senha1 = request.POST.get("senha1")
        senha2 = request.POST.get("senha2")

        if not senha1 or not senha2:
            messages.error(request, "Não pode deixar as senhas em branco!")
            return render(request, 'contas/edit_cadastro.html')

        if len(senha1)<8:
            messages.error(request, "Senha muito curta!")
            return render(request, 'contas/edit_cadastro.html')

        if senha1 != senha2:
            messages.error(request, "Senhas diferentes!")
            return render(request, 'contas/edit_cadastro.html')

        user = get_object_or_404(User, username=request.user)

        user.set_password(senha1)
        user.save()

        messages.success(request, "Senha alterada com sucesso")

        return redirect('login')

    # user = get_object_or_404(User, username=request.GET.get(user.username))
    return render(request, 'contas/edit_cadastro.html')
