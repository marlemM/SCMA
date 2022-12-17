from django.contrib import admin
from django.urls import path, include
from .views import homeI, salvarI, editarI, updateI, deleteI

urlpatterns = [
    path('', homeI),
    path('salvar/', salvarI, name="salvarI"),
    path('editar/<int:id>', editarI, name="editarI"),
    path('update/<int:id>', updateI, name="updateI"),
    path('delete/<int:id>', deleteI, name="deleteI"),
]
