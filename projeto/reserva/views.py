from django.shortcuts import render, redirect
from .models import Reserva
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def homeR(request):
    reservar = Reserva.objects.all()
    return render(request, "indexreserva.html", {"reservar": reservar})