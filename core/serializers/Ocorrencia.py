from rest_framework import serializers
from core.models import Ocorrencia


class OcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = [
            'id',
            'tipo',
            'gravidade',
            'descricao',
            'providencias',
            'residente',
        ]