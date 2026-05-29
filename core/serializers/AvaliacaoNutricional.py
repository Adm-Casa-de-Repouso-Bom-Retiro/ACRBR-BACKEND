from rest_framework import serializers
from core.models import AvaliacaoNutricional


class AvaliacaoNutricionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvaliacaoNutricional
        fields = [
            'id',
            'peso_kg',
            'altura_cm',
            'imc',
            'restricoes_alimentares',
            'dieta_prescrita',
            'data_avaliacao',
            'residente',
        ]