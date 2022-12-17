from django.shortcuts import render, redirect
from .models import Item
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def homeI(request):
    itens = Item.objects.all()
    return render(request, "indexitem.html", {"itens": itens})

@require_http_methods(["POST"])
def salvarI(request):
    vnome = request.POST.get("nome")
    Item.objects.create(nome=vnome)
    itens = Item.objects.all()
    return redirect('/item')

@require_http_methods(["GET"])
def editarI(request, id):
    itens = Item.objects.get(id=id)
    return render(request, "updateitem.html", {"itens": itens})

@require_http_methods(["POST"])
def updateI(request, id):
    vnome = request.POST.get("nome")
    item = Item.objects.get(id=id)
    item.nome = vnome
    item.save()
    return redirect(homeI)

@require_http_methods(["GET"])
def deleteI(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect(homeI)