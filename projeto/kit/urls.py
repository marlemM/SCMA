from django.contrib import admin
from django.urls import path, include
from .views import homeK, salvarK, editarK, updateK, deleteK, preencher, remover

urlpatterns = [
    path('', homeK),
    path('salvar/', salvarK, name="salvar"),
    path('editar/<int:id>', editarK, name="editar"),
    path('update/<int:id>', updateK, name="update"),
    path('delete/<int:id>', deleteK, name="delete"),
    path('preencher/<int:id>', preencher, name="preencher"),
    path('remover/<int:id>', remover, name="remover"),
]
