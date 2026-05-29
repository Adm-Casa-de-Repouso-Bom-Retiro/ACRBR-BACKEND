from rest_framework import serializers
from core.models import PedidosMedicamento


class PedidosMedicamentoSerializer(serializers.ModelSerializer):
    medicamento_nome = serializers.CharField(
        source='medicamentos.nome_comercial',
        read_only=True
    )

    class Meta:
        model = PedidosMedicamento
        fields = [
            'id',
            'qtd_solicitada',
            'data_pedido',
            'data_entrega',
            'medicamentos',
            'medicamento_nome',
            'medicamentos_estoque',
        ]