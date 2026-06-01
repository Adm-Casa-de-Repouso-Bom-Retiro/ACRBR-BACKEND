from django.db import models


class MedicamentosPrescricao(models.Model):

    prescricao = models.ForeignKey(
        'core.Prescricao',
        on_delete=models.CASCADE,
        related_name='medicamentos_prescricao',
    )
    medicamento = models.ForeignKey(
        'core.Medicamento',
        on_delete=models.CASCADE,
        related_name='prescricoes_medicamento',
    )
    dosagem = models.CharField(max_length=45, blank=True)
    frequencia = models.CharField(max_length=45, blank=True)
    arquivo_receita = models.CharField(max_length=255, blank=True)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)

    def __str__(self):
        return (
            f'Prescrição #{self.prescricao_id} — '
            f'Medicamento: {self.medicamento}'
        )