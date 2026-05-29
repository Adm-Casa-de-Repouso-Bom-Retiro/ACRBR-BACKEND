from rest_framework import serializers
from core.models import MedicamentosPrescricao


class MedicamentosPrescricaoSerializer(serializers.ModelSerializer):
    medicamento_nome = serializers.CharField(
        source='medicamento.nome_comercial',
        read_only=True
    )

    prescricao_data = serializers.DateField(
        source='prescricao.data',
        read_only=True
    )

    class Meta:
        model = MedicamentosPrescricao
        fields = [
            'id',
            'prescricao',
            'prescricao_data',
            'medicamento',
            'medicamento_nome',
            'dosagem',
            'frequencia',
            'arquivo_receita',
            'data_inicio',
            'data_fim',
        ]