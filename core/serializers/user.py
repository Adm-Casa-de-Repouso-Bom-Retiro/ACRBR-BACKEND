from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from core.models import Administrador
from uploader.models import Image


class AdministradorSerializer(ModelSerializer):
    foto_url = serializers.SerializerMethodField()

    class Meta:
        model = Administrador
        fields = [
            'id',
            'email',
            'nome',
            'telefone',
            'cargo',
            'data_registro',
            'foto_url',
            'is_active',
            'is_staff',
            'is_superuser',
            'last_login',
            'groups',
        ]
        depth = 1

    def get_foto_url(self, obj):
        if obj.foto and obj.foto.file:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.foto.file.url)
            return obj.foto.file.url
        return None


class AdministradorRegistrationSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    data_registro = serializers.DateField(
        format='%d/%m/%Y',
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],
        required=False,
    )
    perfil_attachment_key = serializers.UUIDField(write_only=True, required=False)

    class Meta:
        model = Administrador
        fields = ['id', 'email', 'nome', 'telefone', 'cargo', 'data_registro', 'password', 'perfil_attachment_key']

    def create(self, validated_data):
        attachment_key = validated_data.pop('perfil_attachment_key', None)

        administrador = Administrador.objects.create_user(**validated_data)

        if attachment_key:
            try:
                imagem = Image.objects.get(attachment_key=attachment_key)
                administrador.foto = imagem
                administrador.save()
            except Image.DoesNotExist:
                pass

        return administrador