from django.db import models


class RotinaResidentes(models.Model):

    DIAS_SEMANA_CHOICES = [
        ('segunda', 'Segunda-feira'),
        ('terca', 'Terça-feira'),
        ('quarta', 'Quarta-feira'),
        ('quinta', 'Quinta-feira'),
        ('sexta', 'Sexta-feira'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo'),
        ('diario', 'Diário'),
    ]

    categoria = models.CharField(max_length=45, blank=True)
    descricao = models.CharField(max_length=200, blank=True)
    horario = models.TimeField()
    dias_semana = models.CharField(
        max_length=20,
        choices=DIAS_SEMANA_CHOICES,
        blank=True,
    )
    residente = models.ForeignKey(
        'core.Residente',
        on_delete=models.CASCADE,
        related_name='rotinas',
    )

    def __str__(self):
        return f'Rotina #{self.pk} — {self.categoria} ({self.horario})'