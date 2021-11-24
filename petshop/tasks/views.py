
from django.shortcuts import render, redirect
from rest_framework import generics
from tasks.serializer import TodoSerializers
from .models import Task

from .forms import AddData
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages



def Pagina(request):
    return render(request, 'tasks/pagina_principal.html')


def Sucesso(request):
    return render(request, 'tasks/sucesso.html')



@login_required
def Cadastro(request):
    if request.method == 'POST':
        form = AddData(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'pendente'
            task.user = request.user
            task.save()
            
        return render(request, 'tasks/sucesso.html')
    else:
        form = AddData()
        return render(request, 'tasks/cadastro.html', {'form' : form })

        
@login_required
def Login(request):
    return render(request, 'tasks/login.html')


@login_required
def Usuario(request):
    table = Task.objects.all()
    tasks_list = Task.objects.all().order_by('-created_at').filter(user=request.user)
    paginator = Paginator(tasks_list, 4)
    page = request.GET.get('page')
    tasks = paginator.get_page(page)
    return render(request, 'tasks/tela_usuario.html', {'tasks': tasks, 'table': table})
    

def Sobre(request):
    return render(request, 'about/sobre_nos.html')


class ListAndCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoSerializers


class DetailAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoSerializers


