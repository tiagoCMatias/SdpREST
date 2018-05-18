from rest_framework import serializers

from sdp.models.estrutura.componentes.componente import Componente


class ComponentesSerializer(serializers.ModelSerializer):

    def to_representation(self, obj):
        data = super(ComponentesSerializer, self).to_representation(obj)  # the original data
        return data

    class Meta:
        model = Componente
        fields = '__all__'