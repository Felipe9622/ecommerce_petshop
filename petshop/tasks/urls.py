from django.urls import path, include
from . import views
from tasks.views import DetailAndDelete, ListAndCreate


urlpatterns = [
    path('', views.Pagina),
    path('usuario/cadastro/', views.Cadastro, name="cadastro"),
    path('sucesso/', views.Sucesso, name="Sucesso"),
    path('login/', views.Login, name="login"),
    path('usuario/', views.Usuario),
    path('sobre_nos/', views.Sobre),
    path('dados/', ListAndCreate.as_view()),
    path('dados/<int:pk>/', DetailAndDelete.as_view()),
]
