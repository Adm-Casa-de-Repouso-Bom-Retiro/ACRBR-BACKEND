from rest_framework import serializers
from core.models import RotinaResidentes


class RotinaResidentesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RotinaResidentes
        fields = [
            'id',
            'categoria',
            'descricao',
            'horario',
            'dias_semana',
            'residente',
        ]