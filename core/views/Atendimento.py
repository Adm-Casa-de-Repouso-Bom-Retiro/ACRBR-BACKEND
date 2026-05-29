from rest_framework.viewsets import ModelViewSet
from core.models import Atendimento
from core.serializers import AtendimentoSerializer


class AtendimentoViewSet(ModelViewSet):
    queryset = Atendimento.objects.all()
    serializer_class = AtendimentoSerializer