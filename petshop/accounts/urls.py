from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.SignUp.as_view(), name="signup"),

]
