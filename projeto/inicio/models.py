from django.db import models

class Inicio(models.Model):
    nome = models.CharField(max_length=100)

    def __srt__(self):
        return self.nome