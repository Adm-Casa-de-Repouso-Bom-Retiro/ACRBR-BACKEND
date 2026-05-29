from rest_framework.viewsets import ModelViewSet

from core.models import MedicamentosPrescricao
from core.serializers import MedicamentosPrescricaoSerializer

class MedicamentosPrescricaoViewSet(ModelViewSet):
    queryset = MedicamentosPrescricao.objects.all()
    serializer_class = MedicamentosPrescricaoSerializer