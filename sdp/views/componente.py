from sdp.models.estrutura.componentes.componente import Componente
from rest_framework import viewsets
from sdp.serializers.componente import ComponenteSerializer

class ConfigTendaViewSet(viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Componente.objects.all().order_by('-id')
    serializer_class = ComponenteSerializer