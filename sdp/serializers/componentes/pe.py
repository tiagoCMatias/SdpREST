from rest_framework import serializers

from sdp.models.estrutura.componentes.Pe.pe import Pe

class PeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pe
        fields = '__all__'