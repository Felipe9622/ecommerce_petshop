from django.urls import path, include
from . import views
from tasks.views import Petshop_change_and_delete, Petshop_list


urlpatterns = [
    path('', views.Pagina),
    path('cadastro/', views.Cadastro, name="new-data"),
    path('login/', views.Login, name="new-data"),
    path('usuario/', views.Usuario, name="new-data"),
    path('dados/', Petshop_list),
    path('dados/<int:pk>/', Petshop_change_and_delete),


]
