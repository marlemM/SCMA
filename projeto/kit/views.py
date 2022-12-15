from django.shortcuts import render, redirect
from .models import Kit
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def home(request):
    kits = Kit.objects.all()
    return render(request, "indexkit.html", {"kits": kits})

@require_http_methods(["POST"])
def salvar(request):
    vnome = request.POST.get("nome")
    Kit.objects.create(nome=vnome)
    kits = Kit.objects.all()
    return render(request, "indexkit.html", {"kits": kits})

@require_http_methods(["GET"])
def editar(request, id):
    kits = Kit.objects.get(id=id)
    return render(request, "updatekit.html", {"kits": kits})

@require_http_methods(["POST"])
def update(request, id):
    vnome = request.POST.get("nome")
    kit = Kit.objects.get(id=id)
    kit.nome = vnome
    kit.save()
    return redirect(home)

@require_http_methods(["GET"])
def delete(request, id):
    kit = Kit.objects.get(id=id)
    kit.delete()
    return redirect(home)

@require_http_methods(["GET"])
def detalhar(request):
    kits = Kit.objects.all()
    return render(request, "detalhar.html", {"kits": kits})