"""
AlergiaRestricao model.
"""
from django.db import models


class AlergiaRestricao(models.Model):
    """Alergias e restrições do residente."""

    tipo = models.CharField(max_length=45, blank=True)
    descricao = models.CharField(max_length=200, blank=True)
    gravidade = models.CharField(max_length=45, blank=True)
    providencia = models.CharField(max_length=45, blank=True)
    residente = models.ForeignKey(
        'core.Residente',
        on_delete=models.CASCADE,
        related_name='alergias_restricoes',
    )

    def __str__(self):
        return f'Alergia/Restrição #{self.pk} — {self.tipo}'