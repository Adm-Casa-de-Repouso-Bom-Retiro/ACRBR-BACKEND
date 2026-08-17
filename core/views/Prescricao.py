from rest_framework.viewsets import ModelViewSet

from core.models import Prescricao
from core.serializers import PrescricaoSerializer


class PrescricaoViewSet(ModelViewSet):
    queryset = Prescricao.objects.all()
    serializer_class = PrescricaoSerializer
