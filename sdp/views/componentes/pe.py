from sdp.models.estrutura.componentes.Pe.pe import Pe
from rest_framework import viewsets
from sdp.serializers.componentes.pe import PeSerializer

class PeViewModel(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Pe.objects.all().order_by('-id')
    serializer_class = PeSerializer