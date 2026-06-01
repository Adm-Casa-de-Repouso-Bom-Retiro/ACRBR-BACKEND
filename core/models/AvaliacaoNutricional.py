from django.db import models


class AvaliacaoNutricional(models.Model):

    peso_kg = models.DecimalField(max_digits=5, decimal_places=2)
    altura_cm = models.DecimalField(max_digits=5, decimal_places=2)
    imc = models.DecimalField(max_digits=5, decimal_places=2)
    restricoes_alimentares = models.TextField(blank=True)
    dieta_prescrita = models.TextField(blank=True)
    data_avaliacao = models.DateField()
    residente = models.ForeignKey(
        'core.Residente',
        on_delete=models.CASCADE,
        related_name='avaliacoes_nutricionais',
    )

    def __str__(self):
        return f'Avaliação Nutricional #{self.pk} — {self.data_avaliacao}'