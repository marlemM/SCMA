from django.test import TestCase
from django.urls import reverse

class UsuarioViewTests(TestCase):

    def test_login_usuario(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
