from django.shortcuts import render, redirect
from .models import Item
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def home(request):
    Itens = Item.objects.all()
    return render(request, "indexitem.html", {"Itens": Itens})

@require_http_methods(["POST"])
def salvar(request):
    vnome = request.POST.get("nome")
    Item.objects.create(nome=vnome)
    Itens = Item.objects.all()
    return render(request, "indexitem.html", {"Itens": Itens})

@require_http_methods(["GET"])
def editar(request, id):
    Itens = Item.objects.get(id=id)
    return render(request, "update.html", {"Itens": Itens})

@require_http_methods(["POST"])
def update(request, id):
    vnome = request.POST.get("nome")
    item = Item.objects.get(id=id)
    item.nome = vnome
    item.save()
    return redirect(home)

@require_http_methods(["GET"])
def delete(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect(home)

@require_http_methods(["GET"])
def detalhar(request):
    Itens = Item.objects.all()
    return render(request, "detalhar.html", {"Itens": Itens})