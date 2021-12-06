
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from ecommerce.models import Category, Product
from tasks.serializer import TodoSerializers
from .models import Task
from .forms import AddData
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages


#paginas sem usuario estar logado begin
def Pagina(request):
    data = Product.objects.filter(is_featured=True).order_by('-id')
    return render(request, 'tasks/pagina_principal.html', {'data': data})


def Sobre(request):
    return render(request, 'about/sobre_nos.html')


#begin ecommerce

#categoria dos produtos
def Ecommerce_Categorias(request):
    data = Category.objects.all().order_by('-id')
    return render(request, 'e-commerce/ecommerce_categorias.html', {'data': data})

#lista de produtos
def Ecommerce_Categoias_lista(request, product_id):
    category = Category.objects.get(id=product_id) 
    data = Product.objects.filter(category=category).order_by('-id')  # interage o banco Category com o banco Product, objects.filter pega todos os dados do banco 
    return render(request, 'e-commerce/ecommerce_categorias_lista.html', {'data': data})

#detalhes dos produtos
def Detalhes_Produtos(request,id):
    data = Product.objects.get(id=id)
    related_products = Product.objects.filter(category=data.category).exclude(id=id)[:3]
    return render(request, 'e-commerce/product_detail.html', {'data': data, 'related_products': related_products})



#ecommerce end

#paginas sem usuario estar logado end


#paginas com usuario logado begin
@login_required
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

#paginas com usuario logado end 
    




class ListAndCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoSerializers


class DetailAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoSerializers

#barra de pesquisa
def Pesquisa(request):
    q=request.get['q']
    data = Product.objects.filter(title__icontains=q).order_by('-id')
    return render(request, 'tasks/search.html', {'data': data})
