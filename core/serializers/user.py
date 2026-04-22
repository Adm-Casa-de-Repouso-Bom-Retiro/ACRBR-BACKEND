from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from core.models import Administrador


class AdministradorSerializer(ModelSerializer):
    class Meta:
        model = Administrador
        fields = [
            'id',
            'email',
            'nome',
            'telefone',
            'cargo',
            'data_registro',
            'is_active',
            'is_staff',
            'is_superuser',
            'last_login',
            'groups',
        ]
        depth = 1


class AdministradorRegistrationSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    data_registro = serializers.DateField(format='%d/%m/%Y', input_formats=['%d/%m/%Y', '%Y-%m-%d'], required=False)

    class Meta:
        model = Administrador
        fields = ['id', 'email', 'nome', 'telefone', 'cargo', 'data_registro', 'password']

    def create(self, validated_data):
        return Administrador.objects.create_user(**validated_data)
