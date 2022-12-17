from django.contrib import admin
from django.urls import path, include
from .views import homeR

urlpatterns = [
    path('', homeR),
]