from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Home do projeto
def home(request):
    return render(request, 'home.html')


def cadastro(request):
    
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password1'])
                user.last_name = request.POST['last_name']
                user.save()

                login(request, user)
                return redirect('home')

            except:
                return render(request, 'cadastro.html',
                              {
                              'form': UserCreationForm,
                              'error': 'Usuário já existe!'
                              } )
                              
        return render(request, 'cadastro.html',
                              {
                              'form': UserCreationForm,
                              'error': 'Senhas não são iguais!!'
                              })


def Login(request):

    return render(request, 'login.html')