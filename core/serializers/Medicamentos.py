from rest_framework import serializers
from core.models import Medicamento

class MedicamentoSerializer(serializers.ModelSerializer):
    estoque_atual = serializers.IntegerField(
        source='estoque_medicamentos.quantidade_atual',
        read_only=True
    )

    class Meta:
        model = Medicamento
        fields = '__all__'