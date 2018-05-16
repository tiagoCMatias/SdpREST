from rest_framework import serializers

from sdp.models.estrutura.componentes.Viga.viga import Viga

class VigaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viga
        fields = '__all__'