from django.shortcuts import render, redirect
from .models import Inicio
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def home(request):
    kits = Inicio.objects.all()
    return render(request, "index.html", {"kits": kits})
