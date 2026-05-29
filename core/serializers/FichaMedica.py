from rest_framework import serializers
from core.models import FichaMedica


class FichaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichaMedica
        fields = [
            'id',
            'tipo_sanguineo',
            'grau_dependencia',
            'status_paciente',
            'doencas_cronicas',
            'observacoes',
            'residente',
        ]