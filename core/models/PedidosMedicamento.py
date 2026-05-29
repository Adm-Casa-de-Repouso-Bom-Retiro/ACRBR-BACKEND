"""
PedidosMedicamento model.
"""
from django.db import models


class PedidosMedicamento(models.Model):
    """Pedidos de reposição de estoque."""

    qtd_solicitada = models.IntegerField()
    data_pedido = models.DateField()
    data_entrega = models.DateField(null=True, blank=True)
    medicamentos = models.ForeignKey(
        'core.Medicamento',
        on_delete=models.CASCADE,
        related_name='pedidos',
    )
    medicamentos_estoque = models.ForeignKey(
        'core.EstoqueMedicamentos',
        on_delete=models.CASCADE,
        related_name='pedidos',
    )

    def __str__(self):
        return f'Pedido #{self.pk} — {self.data_pedido}'