from rest_framework import serializers
from core.models import DadosMedicos, MedicacaoDadosMedicos


class MedicacaoDadosMedicosSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicacaoDadosMedicos
        fields = ['id', 'nome', 'dosagem', 'horario']


class DadosMedicosSerializer(serializers.ModelSerializer):
    medicacoes = MedicacaoDadosMedicosSerializer(many=True, required=False)

    class Meta:
        model = DadosMedicos
        fields = [
            'id',
            'condicoes_medicas',
            'alergias',
            'observacoes',
            'peso_altura',
            'peso',
            'altura',
            'sem_alergias_conhecidas',
            'residente',
            'medicacoes',
        ]
        extra_kwargs = {
            'peso': {'required': False, 'allow_null': True},
            'altura': {'required': False, 'allow_null': True},
        }

    def create(self, validated_data):
        medicacoes_data = validated_data.pop('medicacoes', [])
        dados_medicos = DadosMedicos.objects.create(**validated_data)

        for medicacao_data in medicacoes_data:
            MedicacaoDadosMedicos.objects.create(
                dados_medicos=dados_medicos,
                **medicacao_data,
            )

        return dados_medicos

    def update(self, instance, validated_data):
        medicacoes_data = validated_data.pop('medicacoes', [])

        instance.condicoes_medicas = validated_data.get(
            'condicoes_medicas', instance.condicoes_medicas
        )
        instance.alergias = validated_data.get('alergias', instance.alergias)
        instance.observacoes = validated_data.get('observacoes', instance.observacoes)
        instance.peso_altura = validated_data.get('peso_altura', instance.peso_altura)
        instance.peso = validated_data.get('peso', instance.peso)
        instance.altura = validated_data.get('altura', instance.altura)
        instance.sem_alergias_conhecidas = validated_data.get(
            'sem_alergias_conhecidas', instance.sem_alergias_conhecidas
        )
        instance.save()

        instance.medicacoes.all().delete()

        for medicacao_data in medicacoes_data:
            MedicacaoDadosMedicos.objects.create(
                dados_medicos=instance,
                **medicacao_data,
            )

        return instance
