from rest_framework.viewsets import ModelViewSet

from core.models import AvaliacaoNutricional
from core.serializers import AvaliacaoNutricionalSerializer


class AvaliacaoNutricionalViewSet(ModelViewSet):
    queryset = AvaliacaoNutricional.objects.all()
    serializer_class = AvaliacaoNutricionalSerializer