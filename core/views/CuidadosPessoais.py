from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.models import CuidadosPessoais
from core.serializers import CuidadosPessoaisSerializer


class CuidadosPessoaisViewSet(ModelViewSet):
    queryset = CuidadosPessoais.objects.all()
    serializer_class = CuidadosPessoaisSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['residente']
