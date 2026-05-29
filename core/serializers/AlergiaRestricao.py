from rest_framework import serializers
from core.models import AlergiaRestricao


class AlergiaRestricaoSerializer(serializers.ModelSerializer):
    residente_nome = serializers.CharField(
        source='residente.nome_responsavel',
        read_only=True
    )

    class Meta:
        model = AlergiaRestricao
        fields = [
            'id',
            'tipo',
            'descricao',
            'gravidade',
            'providencia',
            'residente',
            'residente_nome',
        ]