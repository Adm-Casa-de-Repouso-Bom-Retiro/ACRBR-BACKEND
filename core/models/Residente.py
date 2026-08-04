from django.db import models
from uploader.models import Image

GRAU_DEPENDENCIA_CHOICES = (
    ('grau_1', 'Grau 1 - Independente'),
    ('grau_2', 'Grau 2 - Necessita auxílio parcial'),
    ('grau_3', 'Grau 3 - Dependência total'),
)


class Residente(models.Model):

    foto = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='residentes',
    )

    # Dados do residente
    nome_completo = models.CharField(max_length=150, default='')
    data_nascimento = models.DateField(null=True, blank=True)
    quarto = models.CharField(max_length=20, blank=True, default='')
    grau_dependencia = models.CharField(
        max_length=10,
        choices=GRAU_DEPENDENCIA_CHOICES,
        blank=True,
        default='',
    )
    observacoes = models.TextField(blank=True, default='')
    plano_saude = models.CharField(max_length=80, blank=True)
    data_admissao = models.DateTimeField()
    data_saida = models.DateTimeField(null=True, blank=True)

    # Responsável 1
    nome_responsavel = models.CharField(max_length=150)
    telefone_responsavel = models.CharField(max_length=14)
    parentesco = models.CharField(max_length=40, blank=True)

    # Responsável 2
    nome_responsavel_2 = models.CharField(max_length=150, blank=True, default='')
    telefone_responsavel_2 = models.CharField(max_length=14, blank=True, default='')
    parentesco_2 = models.CharField(max_length=40, blank=True, default='')

    dados_residentes = models.ForeignKey(
        'core.Administrador',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='residentes_gerenciados',
    )

    def __str__(self):
        return f'Residente #{self.pk} — {self.nome_completo}'