from rest_framework import serializers

from core.models import AnotacaoCalendario


class AnotacaoCalendarioSerializer(serializers.ModelSerializer):
    autor_nome = serializers.SerializerMethodField()
    hora = serializers.TimeField(allow_null=True, required=False, input_formats=['%H:%M', '%H:%M:%S'])

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

    def validate_hora(self, value):
        if value in ['', None]:
            return None
        return value

    def to_internal_value(self, data):
        if isinstance(data, dict):
            data = data.copy()
            if data.get('hora') == '':
                data['hora'] = None
            if data.get('texto') == '':
                data['texto'] = ''
        return super().to_internal_value(data)
