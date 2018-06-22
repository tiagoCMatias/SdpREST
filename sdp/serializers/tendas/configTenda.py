from rest_framework import serializers

from sdp.models.Tendas.configTenda import ConfigTenda

class ConfigTendaSerializer(serializers.ModelSerializer):

    def to_representation(self, obj):
        data = super(ConfigTendaSerializer, self).to_representation(obj)  # the original data
        return data

    class Meta:
        model = ConfigTenda
        fields = '__all__'