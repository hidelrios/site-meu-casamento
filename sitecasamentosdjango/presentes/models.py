from django.db import models

class Presente(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    reservado_por = models.CharField(max_length=200, blank=True, null=True)
    reservado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
