from rest_framework import serializers
from core.models import AplicacaoMedicamentos


class AplicacaoMedicamentosSerializer(serializers.ModelSerializer):
    medicamento_prescrito_id = serializers.IntegerField(
        source='medicamentos_prescricao.id',
        read_only=True
    )

    class Meta:
        model = AplicacaoMedicamentos
        fields = [
            'id',
            'data_hora_prevista',
            'data_hora_aplicacao',
            'aplicado',
            'motivo_nao_aplicado',
            'medicamentos_prescricao',
            'medicamento_prescrito_id',
        ]