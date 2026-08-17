from rest_framework.viewsets import ModelViewSet

from core.models import Residente
from core.serializers import ResidenteSerializer


class ResidenteViewSet(ModelViewSet):
    queryset = Residente.objects.all()
    serializer_class = ResidenteSerializer
