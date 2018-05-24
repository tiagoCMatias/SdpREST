from rest_framework import serializers

from sdp.models.estrutura.listaComponentes import ListaDeComponentes
from sdp.serializers.tendas.configTenda import ConfigTendaSerializer


class ListaDeComponentesSerializer(serializers.ModelSerializer):

    def to_representation(self, obj):
        data = super(ListaDeComponentesSerializer, self).to_representation(obj)  # the original data
        return data

    class Meta:
        model = ListaDeComponentes
        fields = ('componente', 'tenda')


class FullListaDeComponentesSerializer(serializers.ModelSerializer):
    tenda = ConfigTendaSerializer(many=False, read_only=True)

    def to_representation(self, obj):
        data = super(FullListaDeComponentesSerializer, self).to_representation(obj)  # the original data
        return data

    class Meta:
        model = ListaDeComponentes
        fields = ('componente', 'tenda')