from django.test import TestCase
from django.urls import reverse
import os
import django
from .models import Usuario

class Usuario_test(TestCase):

    def test_create_usuario(self):

        usuario = Usuario(nome='fulano', email='fulano@fu.com', senha='12345678')
        self.assertEqual('fulano', usuario.nome)
        self.assertEqual('fulano@fu.com', usuario.email)
        self.assertEqual('12345678', usuario.senha)

    def test_create_usuario2(self):
        usuario = Usuario(nome='ciclano', email='ciclano@fu.com', senha='87654321')
        self.assertEqual('87654321', usuario.senha)




# Create your tests here.
