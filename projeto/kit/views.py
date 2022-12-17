from django.shortcuts import render, redirect
from .models import Kit
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def homeK(request):
    kits = Kit.objects.all()
    return render(request, "indexkit.html", {"kits": kits})

@require_http_methods(["POST"])
def salvarK(request):
    vnome = request.POST.get("nome")
    Kit.objects.create(nome=vnome)
    kits = Kit.objects.all()
    return render(request, "indexkit.html", {"kits": kits})

@require_http_methods(["GET"])
def editarK(request, id):
    kits = Kit.objects.get(id=id)
    return render(request, "updatekit.html", {"kits": kits})

@require_http_methods(["POST"])
def updateK(request, id):
    vnome = request.POST.get("nome")
    kit = Kit.objects.get(id=id)
    kit.nome = vnome
    kit.save()
    return redirect(homeK)

@require_http_methods(["GET"])
def deleteK(request, id):
    kit = Kit.objects.get(id=id)
    kit.delete()
    return redirect(homeK)

@require_http_methods(["GET"])
def detalharK(request):
    kits = Kit.objects.all()
    return render(request, "detalhar.html", {"kits": kits})