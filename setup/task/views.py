from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django import forms
from .forms import RendaForm, DespesaForm
from .models import Renda, Despesa

class RendaForm(forms.ModelForm):
    class Meta:
        model = Renda
        fields = ['valor', 'data']


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


def esqueci_senha(request):
    return render(request, 'auth/esqueci_senha.html')


def perg_freq(request):
    return render(request, 'auth/perg_freq.html')


# Tarefas refere-se ao cadastro das depesas 
@login_required   
def tarefa_despesa(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('despesas')
        else:
            return render(request, 'main/tarefa_despesa.html', {
                'form': form,
                'error': 'Dados inválidos!'
            })
    else:
        form = DespesaForm()

    return render(request, 'main/tarefa_despesa.html', {'form': form})


# Refere-se ao cadastro da renda pessoal  
@login_required 
def tarefa_renda(request):
    if request.method == 'POST':
        form = RendaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('despesas')
        else:
            return render(request, 'main/tarefa_renda.html', {
                'form': form,
                'error': 'Dados inválidos!'
            })
    else:
        form = RendaForm()

    return render(request, 'main/tarefa_renda.html', {'form': form})


@login_required
def sair(request):
    logout(request)
    return redirect('home')


@login_required
def despesas(request):
    return render(request, 'main/despesas.html')