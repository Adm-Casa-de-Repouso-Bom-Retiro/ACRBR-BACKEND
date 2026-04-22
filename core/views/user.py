from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Administrador
from core.serializers import AdministradorRegistrationSerializer, AdministradorSerializer


class AdministradorViewSet(ModelViewSet):
    queryset = Administrador.objects.all().order_by('id')
    serializer_class = AdministradorSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary='Dados do administrador autenticado',
        description='Retorna os dados do administrador autenticado.',
        responses={200: AdministradorSerializer, 401: None},
    )
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        """Retorna os dados do administrador autenticado."""
        user = request.user
        serializer = AdministradorSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AdministradorRegistrationView(CreateAPIView):
    """Endpoint para registro de novos administradores."""

    queryset = Administrador.objects.all()
    serializer_class = AdministradorRegistrationSerializer
    permission_classes = [AllowAny]
