from django.db import models


class CuidadosPessoais(models.Model):

    ajuda_banho = models.BooleanField(null=True, blank=True)
    ajuda_higiene_intima = models.BooleanField(null=True, blank=True)
    ajuda_higiene_bucal = models.BooleanField(null=True, blank=True)
    ajuda_usar_banheiro = models.BooleanField(null=True, blank=True)
    ajuda_vestir_roupas = models.BooleanField(null=True, blank=True)
    ajuda_locomocao = models.BooleanField(null=True, blank=True)
    risco_queda = models.BooleanField(null=True, blank=True)
    ajuda_alimentar = models.BooleanField(null=True, blank=True)
    possui_restricoes = models.BooleanField(null=True, blank=True)
    observacoes = models.TextField(blank=True)
    residente = models.OneToOneField(
        'core.Residente',
        on_delete=models.CASCADE,
        related_name='cuidados_pessoais',
    )

    def __str__(self):
        return f'Cuidados Pessoais — Residente #{self.residente_id}'
