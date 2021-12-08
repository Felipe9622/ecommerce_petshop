from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from tasks.views import DetailAndDelete, ListAndCreate




urlpatterns = [
    path('', views.Pagina),
    path('search/', views.Pesquisa, name="search"),
    path('cadastro/', views.Cadastro, name="cadastro"),
    path('sucesso/', views.Sucesso, name="Sucesso"),
    path('login/', views.Login, name="login"),
    path('usuario/', views.Usuario, name="usuario"),
    path('sobre_nos/', views.Sobre, name="sobre_nos"),
    path('loja/', views.Ecommerce_Categorias, name="loja"),
    path('loja-produtos/<int:product_id>',views.Ecommerce_Categoias_lista, name="loja-produtos"),
    path('produtos_detalhes/<int:id>', views.Detalhes_Produtos, name="produtos_detalhes"),
    path('dados/', ListAndCreate.as_view()),
    path('dados/<int:pk>/', DetailAndDelete.as_view()),
    path('add-to-cart', views.add_to_cart, name="add_to_cart"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
