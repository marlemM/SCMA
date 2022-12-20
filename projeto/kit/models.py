from django.db import models
from item.models import Item

class Kit(models.Model):
    nome = models.CharField(max_length=100)
    reservado = models.BooleanField(default=False)
    itens = [models.ForeignKey(Item, on_delete=models.DO_NOTHING)]

    def __srt__(self):
        return self.nome