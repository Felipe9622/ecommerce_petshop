
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


@login_required
def Cadastro(request):
    if request.method == 'POST':
        form = AddData(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'pendente'
            task.user = request.user
            task.save()
            return redirect('/')
    else:
        form = AddData()
        return render(request, 'tasks/cadastro.html', {'form' : form })

        
@login_required
def Login(request):
    return render(request, 'tasks/login.html')


@login_required
def Usuario(request):
    tasks_list = Task.objects.all().order_by('-created_at')
    paginator = Paginator(tasks_list,1)
    page = request.GET.get('page')
    tasks = paginator.get_page(page)
    tasks1 = Task.objects.all()
    return render(request, 'tasks/tela_usuario.html', {'tasks1':tasks1})



def Sobre(request):
    return render(request, 'about/sobre_nos.html')



class ListAndCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoSerializers


class DetailAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoSerializers


