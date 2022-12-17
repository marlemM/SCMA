from django.contrib import admin
from django.urls import path, include
from .views import homeK, salvarK, editarK, updateK, deleteK, detalharK

urlpatterns = [
    path('', homeK),
    path('salvar/', salvarK, name="salvar"),
    path('editar/<int:id>', editarK, name="editar"),
    path('update/<int:id>', updateK, name="update"),
    path('delete/<int:id>', deleteK, name="delete"),
    path('detalhar/<int:id>', detalharK, name="detalhar")
]
