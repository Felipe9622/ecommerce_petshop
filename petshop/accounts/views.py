from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy  # tem a mesma funçã que o redirect com a
#diferença que ele redireciona os usuarios
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    # usuario se cadastra e é redirecionado para o login
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'  # este arquivo vem da pasta raiz
