from django.db import models


class EstoqueMedicamentos(models.Model):
    quantidade_atual = models.IntegerField(default=0)
    quantidade_minima = models.IntegerField(default=0)
    data_ultimo_pedido = models.DateField(null=True, blank=True)
    data_prevista_pedido = models.DateField(null=True, blank=True)
    data_validade = models.DateField(null=True, blank=True)
    lote = models.CharField(max_length=45, blank=True)

    def __str__(self):
        return f'Estoque #{self.pk}'


class Medicamento(models.Model):

    nome_comercial = models.CharField(max_length=45)
    fabricante = models.CharField(max_length=45, blank=True)
    unidade_medida = models.CharField(max_length=45, blank=True)
    contraindicacoes = models.TextField(blank=True)
    estoque_medicamentos = models.ForeignKey(
        EstoqueMedicamentos,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='medicamentos',
    )

    def __str__(self):
        return self.nome_comercial