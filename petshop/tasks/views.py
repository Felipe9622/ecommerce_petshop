from django.shortcuts import render, redirect

from tasks.serializer import TodoSerializers
from .models import Task
from .forms import AddData
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def Pagina(request):
    return render(request, 'tasks/pagina_principal.html')


@login_required
def Cadastro(request):
    if request.method == 'POST':
        form = AddData(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            messages.info(request, 'cadastro feito com sucesso')
            return redirect('/')
    else:
        form = AddData()
        return render(request, 'tasks/cadastro.html', {'form' : form })
@login_required
def Login(request):
    return render(request, 'tasks/login.html')


@login_required
def Usuario(request):
    return render(request, 'tasks/tela_usuario.html')


@api_view(['GET', 'POST'])
def Petshop_list(request):
    if request.method == 'GET':
        todo = Task.objects.all()
        Serializer = TodoSerializers(todo, many=True)
        return Response(Serializer.data)
    elif request.method == 'POST':
        Serializer = TodoSerializers(data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data, status=status.HTTP_201_CREATED)
        return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Petshop_change_and_delete(request, pk):
    try:
        todo = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodoSerializers(todo)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TodoSerializers (todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
