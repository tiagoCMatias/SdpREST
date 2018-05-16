from rest_framework import serializers

from sdp.models.estrutura.componentes.componente import Componente

class ComponenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Componente
        fields = '__all__'