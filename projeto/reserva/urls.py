from django.contrib import admin
from django.urls import path, include
from .views import homeR, detalhar, reservar, devolver

urlpatterns = [
    path('', homeR),
    path('detalhar/<int:id>', detalhar, name="detalhar"),
    path('reservar/', reservar, name="reservar"),
    path('devolve/', devolver, name="devolver")
]