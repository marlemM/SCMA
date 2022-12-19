from django.test import TestCase
from django.urls import reverse
import os
import django
from .models import Usuario

class Usuario_test(TestCase):

    def test_create_usuario(self):

        usuario = Usuario(nome='fulano', email='fulano@fu.com', senha='12345678')
        self.assertEqual('fulano', usuario.nome, 'Testanto usuário')




# Create your tests here.
