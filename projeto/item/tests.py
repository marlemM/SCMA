from django.test import TestCase
from django.urls import reverse
import os
import django
from .models import Item

class Item_test(TestCase):

    def test_create_Item(self):

        item = Item(nome='lapis')
        self.assertEqual('lapis', item.nome, 'Testanto item')




# Create your tests here.
