from django.shortcuts import render, redirect
from .models import Kit
from item.models import Item
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
    #return render(request, "indexkit.html", {"kits": kits})
    return redirect('/kit')


@require_http_methods(["GET"])
def editarK(request, id):
    kit = Kit.objects.get(id=id)
    itens = Item.objects.all()
    return render(request, "updatekit.html", {"kit": kit, "itens":itens})

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

@require_http_methods(["POST"])
def preencher(request, id):
    kit = Kit.objects.get(id=id)
    id_item = request.POST.get("preenche")
    item = Item.objects.get(id=id_item)
    kit.itens.append(item)
    item.disp = False
    itens = Item.objects.all()
    return render(request, "updatekit.html", {"kit": kit, "itens":itens})

@require_http_methods(["GET"])
def remover(request, id):
    kit = Kit.objects.get(id=id)
    Kit.delete()
    return redirect(homeK)