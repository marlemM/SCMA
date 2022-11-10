from django.shortcuts import render, redirect
from .models import Kit

def home(request):
    kits = Kit.objects.all()
    return render(request, "index.html", {"kits": kits})

def salvar(request):
    vnome = request.POST.get("nome")
    Kit.objects.create(nome=vnome)
    kits = Kit.objects.all()
    return render(request, "index.html", {"kits": kits})

def editar(request, id):
    kits = Kit.objects.get(id=id)
    return render(request, "update.html", {"kits": kits})

def update(request, id):
    vnome = request.POST.get("nome")
    kit = Kit.objects.get(id=id)
    kit.nome = vnome
    kit.save()
    return redirect(home)

def delete(request, id):
    kit = Kit.objects.get(id=id)
    kit.delete()
    return redirect(home)

def detalhar(request):
    kits = Kit.objects.all()
    return render(request, "detalhar.html", {"kits": kits})