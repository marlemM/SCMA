from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_safe

@require_http_methods(['GET'])
def cadastro(request):
    return render(request, 'cadastro.html')

@require_http_methods(['POST'])
def cadastro_post(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    user = User.objects.filter(username=username).first()

    if user:
        return HttpResponse('Já exxiste um usuário com esse username')

    user = User.objects.create_user(username=username, email=email, password=senha)
    user.save()

    return render(request, 'login.html')

@require_http_methods(['GET'])
def login(request):
    return render(request, 'login.html')
        
@require_http_methods(['POST'])
def login_post(request):
    username = request.POST.get('username')
    senha = request.POST.get('senha')

    user = authenticate(username=username, password=senha)

    if user:
        login_django(request, user)
        return render(request, 'index.html')
    else:
        return HttpResponse('Email ou senha invalidos')

@require_safe
def home(request):
    return render(request, 'index.html')

@require_safe
def  plataforma(request):
    return HttpResponse('plataforma')