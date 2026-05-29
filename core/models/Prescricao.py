"""
Prescricao model.
"""
from django.db import models


class Prescricao(models.Model):
    """Receita / prescrição médica vinculada a uma ficha médica."""

    ficha_medica = models.ForeignKey(
        'core.FichaMedica',
        on_delete=models.CASCADE,
        related_name='prescricoes',
    )
    data = models.DateField()
    motivo = models.CharField(max_length=45, blank=True)
    descricao = models.CharField(max_length=200, blank=True)
    medico = models.CharField(max_length=45, blank=True)

    def __str__(self):
        return f'Prescrição #{self.pk} — {self.data}'