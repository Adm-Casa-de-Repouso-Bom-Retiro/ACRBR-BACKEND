from rest_framework import serializers
from core.models import Prescricao


class PrescricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescricao
        fields = [
            'id',
            'ficha_medica',
            'data',
            'motivo',
            'descricao',
            'medico',
        ]