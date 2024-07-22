from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')


def cadastro(request):
    
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    
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
                return redirect('login')

            except IntegrityError:
                return render(request, 'cadastro.html',
                              {
                              'form': UserCreationForm(),
                              'error': 'Usuário já existe!'
                              } )
                              
        return render(request, 'cadastro.html',
                              {
                              'form': UserCreationForm(),
                              'error': 'Senhas não são iguais!!'
                              })


def Login(request):

    if request.method == 'GET':
        return render(request, 'login.html',
                              {
                              'form': AuthenticationForm
                              } )
    
    else:
        user = authenticate(

        request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'login.html', {

                'form' : AuthenticationForm,
                'error' : 'Email ou senhas estão incorretos!!'
            })
        else:
            login(request, user)
            return redirect('tasks')


@login_required      
def tasks(request):
    return render(request, 'tasks.html')


@login_required
def sair(request):
    logout(request)
    return redirect('home')