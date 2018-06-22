from rest_framework import serializers

from sdp.models.Componentes.ListaDeComponentes import ListaDeComponentes

class ListaDeComponentesSerializer(serializers.ModelSerializer):

    def to_representation(self, obj):
        data = super(ListaDeComponentesSerializer, self).to_representation(obj)  # the original data
        return data

    class Meta:
        model = ListaDeComponentes
        fields = '__all__'