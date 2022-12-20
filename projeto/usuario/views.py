from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256
from django.views.decorators.http import require_http_methods, require_safe

@require_http_methods(["GET"])
def login(request):
    if request.session.get('usuario'):
        return redirect('/inicio/')
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})


@require_http_methods(["GET"])
def cadastro(request):
    if request.session.get('usuario'):
        return redirect('/inicio/')
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

@require_http_methods(["POST"])
def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/cadastro/?status=1')

    if len(senha) < 8:
        return redirect('/cadastro/?status=2')

    usuario = Usuario.objects.filter(email = email)
    if len(usuario) > 0:
        return redirect('/cadastro/?status=3')

    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome = nome, email = email, senha = senha)
        usuario.save()
        return redirect('/cadastro/?status=0')
    except:
        return redirect('/cadastro/status=4')

@require_http_methods(["POST"])
def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()
    
    usuario = Usuario.objects.filter(email = email).filter(senha = senha)
    if len(usuario) == 0:
        return redirect('/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect(f'/inicio/')

@require_safe
def sair(request):
    request.session.flush()
    return redirect('/')


#É ESSE DAQUI