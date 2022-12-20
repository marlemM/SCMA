from django.db import models

class Item(models.Model):
    nome = models.CharField(max_length=100)
    disp = models.BooleanField(default=True)

    def __srt__(self):
        return self.nome