from django.db import models

class Kit(models.Model):
    nome = models.CharField(max_length=100)

    def __srt__(self):
        return self.nome