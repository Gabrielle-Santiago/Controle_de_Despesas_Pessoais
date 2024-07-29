from django.contrib import admin
from django.urls import path, include
from task import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.Login, name='login'),
    path('tarefa_despesa/', views.tarefa_despesa, name='tarefa_despesa'),
    path('tarefa_renda/', views.tarefa_renda, name='tarefa_renda'),
    path('sair/', views.sair, name='sair'),
    path('despesas/', views.despesas, name='despesas'),
    path('login/main/despesas/', views.despesas, name='despesas_dois'),
    path('login/esqueci_senha/', views.esqueci_senha, name='esqueci_senha'),
    path('perg_freq/', views.perg_freq, name='perg_freq'),
    #path('tarefa_renda/main/despesas/', views.despesas, name='despesas_retorno'),
]
