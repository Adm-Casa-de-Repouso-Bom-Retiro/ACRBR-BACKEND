from rest_framework import serializers
from core.models import Atendimento


class AtendimentoSerializer(serializers.ModelSerializer):
    usuario_nome = serializers.CharField(source='user.__str__', read_only=True)

    class Meta:
        model = Atendimento
        fields = [
            'id',
            'tipo',
            'data_hora',
            'evolucao',
            'user',
            'usuario_nome',
            'residente',
        ]