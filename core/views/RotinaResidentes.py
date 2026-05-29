from rest_framework.viewsets import ModelViewSet

from core.models import RotinaResidentes
from core.serializers import RotinaResidentesSerializer

class RotinaResidentesViewSet(ModelViewSet):
    queryset = RotinaResidentes.objects.all()
    serializer_class = RotinaResidentesSerializer