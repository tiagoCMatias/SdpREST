from rest_framework import serializers

from sdp.models.estrutura.listaComponentes import ListaDeComponentes


class ListaDeComponentesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaDeComponentes
        fields = '__all__'