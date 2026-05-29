"""
FichaMedica model.
"""
from django.db import models


class FichaMedica(models.Model):
    """Informações médicas gerais do residente."""

    TIPO_SANGUINEO_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ]

    tipo_sanguineo = models.CharField(
        max_length=3,
        choices=TIPO_SANGUINEO_CHOICES,
        blank=True,
    )
    grau_dependencia = models.IntegerField(default=0)
    status_paciente = models.CharField(max_length=45, blank=True)
    doencas_cronicas = models.TextField(blank=True)
    observacoes = models.CharField(max_length=100, blank=True)
    residente = models.OneToOneField(
        'core.Residente',
        on_delete=models.CASCADE,
        related_name='ficha_medica',
    )

    def __str__(self):
        return f'Ficha Médica — Residente #{self.residente_id}'