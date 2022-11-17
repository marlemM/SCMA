from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastro_post/', views.cadastro_post, name='cadastro_post'),
    path('login/', views.login, name="login"),
    path('login_post/', views.login_post, name="login_post"),
    path('plataforma', views.plataforma, name="plataforma")
]