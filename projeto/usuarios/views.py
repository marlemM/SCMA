from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_safe

@require_http_methods(["GET"])
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        ##matricula = request.POST.get('matricula')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já exxiste um usuário com esse username')

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        ##ver com Taciano a questão de tirar email e por matricula ou como faz
        return HttpResponse('usuario cadastrado com sucesso')

@require_http_methods(["GET"])  
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return HttpResponse('autenticado')
        else:
            return HttpResponse('Email ou senha invalidos')

@require_safe
##@login_required(login_url="/auth/login")
def  plataforma(request):
    return HttpResponse('plataforma')