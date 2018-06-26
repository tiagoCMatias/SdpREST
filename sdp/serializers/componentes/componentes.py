from rest_framework import serializers

from sdp.models.Componentes.componente import Componente
from sdp.serializers.componentes.familiaComponente import FamiliaComponentesSerializer
from sdp.serializers.componentes.TendaToComponent import TendaToComponentSerializer


class ComponentesSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        data = super(ComponentesSerializer, self).to_representation(obj)  # the original data
        return data

    class Meta:
        model = Componente
        fields = '__all__'



class ComponenteFamiliaSerializer(serializers.ModelSerializer):
    familia = FamiliaComponentesSerializer(many=False, read_only=True)
    def to_representation(self, obj):
        data = super(ComponenteFamiliaSerializer, self).to_representation(obj)  # the original data
        return data

    class Meta:
        model = Componente
        fields = '__all__'



class FullComponentesSerializer(serializers.ModelSerializer):
    # familia = FamiliaComponentesSerializer(many=False, read_only=True)
    pertence = TendaToComponentSerializer(many=True, read_only=True)

    def to_representation(self, obj):
        data = super(FullComponentesSerializer, self).to_representation(obj)  # the original data
        return data

    class Meta:
        model = Componente
        fields = '__all__'