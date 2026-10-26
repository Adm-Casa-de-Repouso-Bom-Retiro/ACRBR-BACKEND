from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.models import AnotacaoCalendario
from core.serializers import AnotacaoCalendarioSerializer

CARGOS_COM_EDICAO = ('chefe', 'gerente', 'cuidador')


class PodeEditarAnotacao(BasePermission):
    message = 'Seu cargo não permite criar, editar ou excluir anotações.'

    def has_permission(self, request, view):
        usuario = request.user

        if not usuario or not usuario.is_authenticated:
            return False

        if request.method in SAFE_METHODS:
            return True

        return usuario.is_superuser or usuario.cargo in CARGOS_COM_EDICAO


class AnotacaoCalendarioViewSet(ModelViewSet):
    queryset = AnotacaoCalendario.objects.select_related('autor').all()
    serializer_class = AnotacaoCalendarioSerializer
    permission_classes = [IsAuthenticated, PodeEditarAnotacao]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['residente', 'data', 'categoria', 'status']

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)
