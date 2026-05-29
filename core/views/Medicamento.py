from rest_framework.viewsets import ModelViewSet

from core.models import Medicamento
from core.serializers import MedicamentoSerializer

class MedicamentosViewSet(ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer