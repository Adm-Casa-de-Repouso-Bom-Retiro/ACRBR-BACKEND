from rest_framework.viewsets import ModelViewSet

from core.models import PedidosMedicamento
from core.serializers import PedidosMedicamentoSerializer

class PedidosMedicamentoViewSet(ModelViewSet):
    queryset = PedidosMedicamento.objects.all()
    serializer_class = PedidosMedicamentoSerializer