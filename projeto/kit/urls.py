from django.contrib import admin
from django.urls import path, include
from .views import homeK, salvarK, editarK, updateK, deleteK, detalharK

urlpatterns = [
    path('', homeK),
    path('salvark/', salvarK, name="salvar"),
    path('editark/<int:id>', editarK, name="editar"),
    path('updatek/<int:id>', updateK, name="update"),
    path('deletek/<int:id>', deleteK, name="delete"),
    path('detalhark/<int:id>', detalharK, name="detalhar")
]
