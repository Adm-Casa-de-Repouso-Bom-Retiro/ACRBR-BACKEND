from django.db import models


class Atendimento(models.Model):

    tipo = models.CharField(max_length=45, blank=True)
    data_hora = models.DateTimeField()
    evolucao = models.TextField(blank=True)
    user = models.ForeignKey(
        'core.Administrador',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='atendimentos',
    )
    residente = models.ForeignKey(
        'core.Residente',
        on_delete=models.CASCADE,
        related_name='atendimentos',
    )

    def __str__(self):
        return f'Atendimento #{self.pk} — {self.data_hora}'