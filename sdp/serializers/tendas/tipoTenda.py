from rest_framework import serializers

from sdp.models.Tendas.tipoTendas import TipoTenda

class TipoTendaSerializer(serializers.ModelSerializer):

    def to_representation(self, obj):
        data = super(TipoTendaSerializer, self).to_representation(obj)  # the original data
        return data

    class Meta:
        model = TipoTenda
        fields = '__all__'