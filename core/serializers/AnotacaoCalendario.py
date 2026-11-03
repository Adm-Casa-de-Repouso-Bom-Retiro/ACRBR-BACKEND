
from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field

from core.models import AnotacaoCalendario


class AnotacaoCalendarioSerializer(serializers.ModelSerializer):
    autor_nome = serializers.SerializerMethodField()

    class Meta:
        model = AnotacaoCalendario

        fields = [
            'id',
            'residente',
            'data',
            'hora',
            'categoria',
            'status',
            'titulo',
            'texto',
            'autor',
            'autor_nome',
            'criado_em',
            'atualizado_em',
        ]

        read_only_fields = [
            'autor',
            'criado_em',
            'atualizado_em',
        ]

    @extend_schema_field(serializers.CharField(allow_null=True))
    def get_autor_nome(self, obj) -> str | None:
        if not obj.autor:
            return None

        return (
            getattr(obj.autor, 'nome', None)
            or getattr(obj.autor, 'email', None)
            or str(obj.autor)
        )
