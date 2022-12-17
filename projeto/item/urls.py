from django.contrib import admin
from django.urls import path, include
from .views import homeI, salvarI, editarI, updateI, deleteI, detalharI

urlpatterns = [
    path('', homeI),
    path('salvar/', salvarI, name="salvar"),
    path('editar/<int:id>', editarI, name="editar"),
    path('update/<int:id>', updateI, name="update"),
    path('delete/<int:id>', deleteI, name="delete"),
    path('detalhar/<int:id>', detalharI, name="detalhar")
]
