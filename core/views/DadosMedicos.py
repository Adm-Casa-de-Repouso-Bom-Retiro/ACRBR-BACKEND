from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.models import DadosMedicos
from core.serializers import DadosMedicosSerializer


class DadosMedicosViewSet(ModelViewSet):
    queryset = DadosMedicos.objects.all()
    serializer_class = DadosMedicosSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['residente']
