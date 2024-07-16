from django.shortcuts import render

# Home do projeto
def home(request):
    return render(request, 'home.html')
