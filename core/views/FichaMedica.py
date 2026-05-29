from rest_framework.viewsets import ModelViewSet

from core.models import FichaMedica
from core.serializers import FichaMedicaSerializer


class FichaMedicaViewSet(ModelViewSet):
    queryset = FichaMedica.objects.all()
    serializer_class = FichaMedicaSerializer