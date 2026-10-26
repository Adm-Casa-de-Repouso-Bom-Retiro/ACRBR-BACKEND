from rest_framework import serializers

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
        read_only_fields = ['autor', 'criado_em', 'atualizado_em']

    def get_autor_nome(self, obj):
        if not obj.autor:
            return None

        return obj.autor.nome or obj.autor.email
