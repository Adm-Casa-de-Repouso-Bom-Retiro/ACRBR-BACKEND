from rest_framework import serializers
from core.models import Residente


class ResidenteSerializer(serializers.ModelSerializer):
    responsavel_nome = serializers.CharField(
        source='dados_residentes.__str__',
        read_only=True
    )

    class Meta:
        model = Residente
        fields = [
            'id',
            'nome_responsavel',
            'telefone_responsavel',
            'parentesco',
            'plano_saude',
            'data_admissao',
            'data_saida',
            'dados_residentes',
            'responsavel_nome',
        ]