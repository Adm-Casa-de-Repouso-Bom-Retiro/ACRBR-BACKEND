from django.db import models

CATEGORIA_CHOICES = (
    ('geral', 'Geral'),
    ('saude', 'Saúde'),
    ('medicacao', 'Medicação'),
    ('alimentacao', 'Alimentação'),
    ('atividade', 'Atividade'),
    ('visita', 'Visita'),
)

STATUS_CHOICES = (
    ('pendente', 'Pendente'),
    ('concluido', 'Concluído'),
    ('nao_concluido', 'Não concluído'),
)


class AnotacaoCalendario(models.Model):

    residente = models.ForeignKey(
        'core.Residente',
        on_delete=models.CASCADE,
        related_name='anotacoes',
    )
    autor = models.ForeignKey(
        'core.Administrador',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='anotacoes_calendario',
    )
    data = models.DateField()
    hora = models.TimeField(null=True, blank=True)
    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIA_CHOICES,
        default='geral',
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pendente',
    )
    titulo = models.CharField(max_length=120)
    texto = models.TextField(blank=True, default='')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['data', 'hora', 'id']
        verbose_name = 'Anotação do calendário'
        verbose_name_plural = 'Anotações do calendário'

    def __str__(self):
        return f'({self.id}) {self.data} — {self.titulo}'
