from django.shortcuts import render, redirect
from .models import Reserva
from kit.models import Kit
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def homeR(request):
    reservas = Reserva.objects.all()
    kits = Kit.objects.all()
    return render(request, "indexreserva.html", {"reservas": reservas,"kits":kits})

@require_http_methods("GET")
def detalhar(request):
    reservar = reservar.objects.all()
    return render(request, "/detalhar")

@require_http_methods("POST")
def reservar(request):
    id_kit = request.POST.get("reserv")
    nome_reservado = Kit.objects.get(id=id_kit).nome
    Reserva.objects.create(nome=nome_reservado)

    kit = Kit.objects.get(id=id_kit)
    kit.reservado = True
    kit.save()
    return redirect(homeR)
    
@require_http_methods("POST")
def devolver(request):
    id_kit = request.POST.get("devolve")
    nome_devolve = Kit.objects.get(id=id_kit).nome
    Reserva.objects.create(nome=nome_devolve)

    kit = Kit.objects.get(id=id_kit)
    kit.reservado = False
    kit.save()
    return redirect(homeR)
