from rest_framework import serializers

from sdp.models.tendas.tipoTendas import TipoTenda

class TipoTendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTenda
        fields = '__all__'