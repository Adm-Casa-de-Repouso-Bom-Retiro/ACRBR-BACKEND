from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import Residente
from uploader.models import Image
from uploader.serializers import ImageSerializer


class ResidenteRetrieveSerializer(ModelSerializer):
    perfil = ImageSerializer(required=False)

    class Meta:
        model = Residente
        fields = '__all__'
        depth = 1


class ResidenteSerializer(serializers.ModelSerializer):
    foto_attachment_key = SlugRelatedField(
        source='foto',
        queryset=Image.objects.all(),
        slug_field='attachment_key',
        required=False,
        write_only=True,
    )

    foto = ImageSerializer(
        required=False,
        read_only=True
    )

    responsavel_nome = serializers.SerializerMethodField()

    class Meta:
        model = Residente
        fields = [
            'id',
            'nome_completo',
            'data_nascimento',
            'quarto',
            'grau_dependencia',
            'observacoes',
            'plano_saude',
            'data_admissao',
            'data_saida',
            'nome_responsavel',
            'telefone_responsavel',
            'parentesco',
            'nome_responsavel_2',
            'telefone_responsavel_2',
            'parentesco_2',
            'dados_residentes',
            'responsavel_nome',
            'foto',
            'foto_attachment_key',
        ]

    def get_responsavel_nome(self, obj):
        return str(obj.dados_residentes) if obj.dados_residentes else None
