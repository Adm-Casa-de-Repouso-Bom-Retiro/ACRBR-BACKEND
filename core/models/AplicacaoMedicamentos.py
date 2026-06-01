from django.db import models


class AplicacaoMedicamentos(models.Model):

    data_hora_prevista = models.DateTimeField()
    data_hora_aplicacao = models.DateTimeField(null=True, blank=True)
    aplicado = models.BooleanField(default=False)
    motivo_nao_aplicado = models.TextField(blank=True)
    medicamentos_prescricao = models.ForeignKey(
        'core.MedicamentosPrescricao',
        on_delete=models.CASCADE,
        related_name='aplicacoes',
    )

    def __str__(self):
        status = 'Aplicado' if self.aplicado else 'Pendente'
        return f'Aplicação #{self.pk} [{status}] — {self.data_hora_prevista}'