from rest_framework.viewsets import ModelViewSet

from core.models import AplicacaoMedicamentos
from core.serializers import AplicacaoMedicamentosSerializer


class AplicacaoMedicamentosViewSet(ModelViewSet):
    queryset = AplicacaoMedicamentos.objects.all()
    serializer_class = AplicacaoMedicamentosSerializer