from rest_framework import serializers
from core.models import CuidadosPessoais


class CuidadosPessoaisSerializer(serializers.ModelSerializer):

    class Meta:
        model = CuidadosPessoais
        fields = [
            'id',
            'ajuda_banho',
            'ajuda_higiene_intima',
            'ajuda_higiene_bucal',
            'ajuda_usar_banheiro',
            'ajuda_vestir_roupas',
            'ajuda_locomocao',
            'risco_queda',
            'ajuda_alimentar',
            'possui_restricoes',
            'observacoes',
            'residente',
        ]
