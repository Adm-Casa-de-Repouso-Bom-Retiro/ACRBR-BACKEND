from rest_framework.viewsets import ModelViewSet

from core.models import AlergiaRestricao
from core.serializers import AlergiaRestricaoSerializer


class AlergiaRestricaoViewSet(ModelViewSet):
    queryset = AlergiaRestricao.objects.all()
    serializer_class = AlergiaRestricaoSerializer