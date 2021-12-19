
from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from ecommerce.models import Category, Product
from tasks.serializer import TodoSerializers
from django.template.loader import render_to_string
from .models import Task
from .forms import AddData
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from django.http import HttpResponse
from tasks.resources import MemberResource,TaskResource

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
    # interage o banco Category com o banco Product, objects.filter pega todos os dados do banco
    data = Product.objects.filter(category=category).order_by('-id')
    return render(request, 'e-commerce/ecommerce_categorias_lista.html', {'data': data})

#detalhes dos produtos
def Detalhes_Produtos(request,id):
    product = Product.objects.get(id=id)
    return render(request, 'e-commerce/product_detail.html', {'data': product})


# estrutura para comando de adicionar pedidos a sacola
def add_to_cart(request):
	# del request.session['cartdata']
	cart_p = {}
    #quando requerir o id solicitados que ele pegue dados especificos do id em que selecionou 
    #como image,title,qty e price 
	cart_p[str(request.GET['id'])] = {
		'image': request.GET['image'],
        'title': request.GET['title'],
		'qty': request.GET['qty'],
		'price': request.GET['price'],
	}
	if 'cartdata' in request.session:
        #se o requerimento for um id valido vai chamar a variavel cartdata
		if str(request.GET['id']) in request.session['cartdata']:
			cart_data = request.session['cartdata']
			cart_data[str(request.GET['id'])]['qty'] = int(
			    cart_p[str(request.GET['id'])]['qty'])
			cart_data.update(cart_data)
			request.session['cartdata'] = cart_data
		else:
			cart_data = request.session['cartdata']
			cart_data.update(cart_p)
			request.session['cartdata'] = cart_data
	else:
		request.session['cartdata'] = cart_p
	return JsonResponse({'data': request.session['cartdata'], 'totalitems': len(request.session['cartdata'])})



# Pagina da sacola de pedidos
#total_amt faz a soma de todos os produtos selecionados no carrinho 
def Cart_list(request):
    total_amt = 0
    for p_id, item in request.session['cartdata'].items():
        total_amt += int(item['qty'])*float(item['price'])
    return render(request, 'e-commerce/cart.html', {'cart_data': request.session['cartdata'], 'totalitems': len(request.session['cartdata']), 'total_amt': total_amt})


#deletar item da Pagina da sacola de pedidos
def delete_cart_item(request):
	p_id = str(request.GET['id'])
	if 'cartdata' in request.session:
		if p_id in request.session['cartdata']:
			cart_data = request.session['cartdata']
			del request.session['cartdata'][p_id]
			request.session['cartdata'] = cart_data
	total_amt = 0
	for p_id, item in request.session['cartdata'].items():
		total_amt += int(item['qty'])*float(item['price'])
	t = render_to_string('ajax/cart_list.html', {'cart_data': request.session['cartdata'], 'totalitems': len(
	    request.session['cartdata']), 'total_amt': total_amt})
	return JsonResponse({'data': t, 'totalitems': len(request.session['cartdata'])})


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
    q=request.GET['q']
    data = Product.objects.filter(title__icontains=q).order_by('-id')
    return render(request, 'tasks/search.html', {'data': data})


def export(request):
    member_resource = MemberResource()
    dataset = member_resource.export()
    #response = HttpResponse(dataset.csv, content_type='text/csv')
    #response['Content-Disposition'] = 'attachment; filename="member.csv"'
    #response = HttpResponse(dataset.json, content_type='application/json')
    #response['Content-Disposition'] = 'attachment; filename="persons.json"'
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response


def export(request):
    task_resource = TaskResource()
    dataset = task_resource.export()
    #response = HttpResponse(dataset.csv, content_type='text/csv')
    #response['Content-Disposition'] = 'attachment; filename="member.csv"'
    #response = HttpResponse(dataset.json, content_type='application/json')
    #response['Content-Disposition'] = 'attachment; filename="persons.json"'
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response
