from django.shortcuts import render, redirect
from .models import Reserva
from kit.models import Kit
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def homeR(request):
    reservar = Reserva.objects.all()
    kits = Kit.objects.all()
    return render(request, "indexreserva.html", {"reservar": reservar,"kits":kits})

@require_http_methods("GET")
def detalhar(request):
    reservar = reservar.objects.all()
    return render(request, "/detalhar")