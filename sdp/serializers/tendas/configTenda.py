from rest_framework import serializers

from sdp.models.tendas.configTenda import ConfigTenda

class ConfigTendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigTenda
        fields = '__all__'