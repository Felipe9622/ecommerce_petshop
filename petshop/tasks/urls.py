from django.urls import path, include
from . import views
from tasks.views import DetailAndDelete, ListAndCreate


urlpatterns = [
    path('', views.Pagina),
    path('cadastro/', views.Cadastro, name="new-data"),
    path('login/', views.Login, name="new-data"),
    path('usuario/', views.Usuario, name="new-data"),
    path('dados/', ListAndCreate.as_view()),
    path('dados/<int:pk>/', DetailAndDelete.as_view()),
]
