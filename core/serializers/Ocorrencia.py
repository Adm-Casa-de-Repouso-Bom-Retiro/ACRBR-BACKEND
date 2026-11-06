from rest_framework import serializers
from rest_framework.serializers import SlugRelatedField

from core.models import Ocorrencia
from uploader.models import Image
from uploader.serializers import ImageSerializer


class OcorrenciaSerializer(serializers.ModelSerializer):
    fotos_attachment_keys = SlugRelatedField(
        source='fotos',
        queryset=Image.objects.all(),
        slug_field='attachment_key',
        many=True,
        required=False,
        write_only=True,
    )
    fotos = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Ocorrencia
        fields = [
            'id',
            'tipo',
            'gravidade',
            'descricao',
            'providencias',
            'residente',
            'fotos',
            'fotos_attachment_keys',
        ]
