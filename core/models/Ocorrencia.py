"""
Ocorrencia model.
"""
from django.db import models


class Ocorrencia(models.Model):
    """Registro de emergências ou problemas com o residente."""

    tipo = models.CharField(max_length=45, blank=True)
    gravidade = models.CharField(max_length=45, blank=True)
    descricao = models.TextField(blank=True)
    providencias = models.TextField(blank=True)
    residente = models.ForeignKey(
        'core.Residente',
        on_delete=models.CASCADE,
        related_name='ocorrencias',
    )

    def __str__(self):
        return f'Ocorrência #{self.pk} — {self.tipo}'