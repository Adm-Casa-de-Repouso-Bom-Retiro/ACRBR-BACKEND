from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class DadosMedicos(models.Model):

    condicoes_medicas = models.TextField(blank=True)
    alergias = models.TextField(blank=True)
    observacoes = models.TextField(blank=True)
    peso_altura = models.CharField(max_length=30, blank=True)
    peso = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(400)],
    )
    altura = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        null=True,
        blank=True,
        validators=[MinValueValidator(30), MaxValueValidator(250)],
    )
    sem_alergias_conhecidas = models.BooleanField(default=False)
    residente = models.OneToOneField(
        'core.Residente',
        on_delete=models.CASCADE,
        related_name='dados_medicos',
    )

    def __str__(self):
        return f'Dados Médicos — Residente #{self.residente_id}'


class MedicacaoDadosMedicos(models.Model):

    nome = models.CharField(max_length=100)
    dosagem = models.CharField(max_length=50, blank=True)
    horario = models.CharField(max_length=100, blank=True)
    dados_medicos = models.ForeignKey(
        'core.DadosMedicos',
        on_delete=models.CASCADE,
        related_name='medicacoes',
    )

    def __str__(self):
        return f'Medicação — {self.nome} (Residente #{self.dados_medicos.residente_id})'
