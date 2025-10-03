from django.db import models

class Convidado(models.Model):
    nome = models.CharField(max_length=200, blank=False, unique=True)
    acompanhantes = models.PositiveIntegerField(default=0)
    contato = models.CharField(max_length=200, unique=True, blank=False)
    confirmado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} (+{self.acompanhantes})"
