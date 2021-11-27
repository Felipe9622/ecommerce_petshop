from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from tasks.views import DetailAndDelete, ListAndCreate



urlpatterns = [
    path('', views.Pagina),
    path('cadastro/', views.Cadastro, name="cadastro"),
    path('sucesso/', views.Sucesso, name="Sucesso"),
    path('login/', views.Login, name="login"),
    path('usuario/', views.Usuario, name="usuario"),
    path('sobre_nos/', views.Sobre, name="sobre_nos"),
    path('loja/', views.Ecommerce, name="loja"),
    path('dados/', ListAndCreate.as_view()),
    path('dados/<int:pk>/', DetailAndDelete.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
