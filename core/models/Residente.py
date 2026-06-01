from django.db import models
from uploader.models import Image


class Residente(models.Model):

    Image,
    nome_responsavel = models.CharField(max_length=150)
    telefone_responsavel = models.CharField(max_length=14)
    parentesco = models.CharField(max_length=40, blank=True)
    plano_saude = models.CharField(max_length=80, blank=True)
    data_admissao = models.DateTimeField()
    data_saida = models.DateTimeField(null=True, blank=True)
    dados_residentes = models.ForeignKey(
        'core.Administrador',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='residentes_gerenciados',
    )

    def __str__(self):
        return f'Residente #{self.pk} — {self.nome_responsavel}'