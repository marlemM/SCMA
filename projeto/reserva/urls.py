from django.contrib import admin
from django.urls import path, include
from .views import homeR, detalhar

urlpatterns = [
    path('', homeR),
    path('detalhar/<int:id>', detalhar, name="detalhar"),
]