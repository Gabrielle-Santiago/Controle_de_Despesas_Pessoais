import os
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Renda
from .forms import RendaForm, DespesaForm
import csv

def home(request):
    return render(request, 'main/home.html')


def cadastro(request):
    
    if request.method == 'GET':
        return render(request, 'auth/cadastro.html')
    
    else:
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        last_name = request.POST['last_name']
        
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password1'])
                
                user.last_name = request.POST['last_name']
                user.save()

                login(request, user)
                return redirect('auth/login')

            except IntegrityError:
                return render(request, 'cadastro.html',
                              {
                              'form': UserCreationForm(),
                              'error': 'Usuário já existe!'
                              } )
                              
        return render(request, 'auth/cadastro.html',
                              {
                              'form': UserCreationForm(),
                              'error': 'Senhas não são iguais!!'
                              })


def Login(request):

    if request.method == 'GET':
        return render(request, 'auth/login.html',
                              {
                              'form': AuthenticationForm
                              } )
    
    else:
        user = authenticate(

        request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'auth/login.html', {

                'form' : AuthenticationForm,
                'error' : 'Email ou senhas estão incorretos!!'
            })
        else:
            login(request, user)
            return redirect('main/despesas')


# Refere-se ao cadastro da renda pessoal  
@login_required 
def tarefa_renda(request):
    if request.method == 'POST':
        form = RendaForm(request.POST)

        if form.is_valid():
            renda = form.save()
            
            renda_CSV = r'C:\xampp\htdocs\Controle_de_Despesas_Pessoais\setup\task\utils\arquivos_CSV\renda.csv'

            # Verifica se o arquivo já existe
            file_exists = os.path.isfile(renda_CSV)

            # Abre o arquivo em modo append
            with open(renda_CSV, 'a', newline='') as file:
                writer = csv.writer(file)
                
                if not file_exists:
                    writer.writerow(['valor', 'data', 'descricao'])
                
                writer.writerow([renda.valor, renda.data, renda.descricao])

            return redirect('despesas')
        
        else:
            return render(request, 'main/tarefa_renda.html', {
                'form': form,
                'error': 'Dados inválidos!'
            })
    else:
        form = RendaForm()

    return render(request, 'main/tarefa_renda.html', {'form': form})


# Tarefas refere-se ao cadastro das depesas 
@login_required   
def tarefa_despesa(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST)

        if form.is_valid():
            despesa =  form.save()
            despesa_CSV = r'C:\xampp\htdocs\Controle_de_Despesas_Pessoais\setup\task\utils\arquivos_CSV\despesa.csv'

            # Verifica se o arquivo já existe
            file_exists = os.path.isfile(despesa_CSV)

            # Abre o arquivo em modo append
            with open(despesa_CSV, 'a', newline='') as file:
                writer = csv.writer(file)
                
                if not file_exists:
                    writer.writerow(['valor', 'data', 'descricao'])
                
                writer.writerow([despesa.valor, despesa.data, despesa.descricao])
            return redirect('despesas')
        else:
            return render(request, 'main/tarefa_despesa.html', {
                'form': form,
                'error': 'Dados inválidos!'
            })
    else:
        form = DespesaForm()

    return render(request, 'main/tarefa_despesa.html', {'form': form})


def esqueci_senha(request):
    return render(request, 'auth/esqueci_senha.html')


def perg_freq(request):
    return render(request, 'auth/perg_freq.html')


@login_required
def sair(request):
    logout(request)
    return redirect('home')


@login_required
def despesas(request):
    return render(request, 'main/despesas.html')

