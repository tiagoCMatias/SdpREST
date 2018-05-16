from rest_framework import serializers

from sdp.models.CRM.cliente import Cliente

class ClienteSerializer(serializers.ModelSerializer):

    def to_representation(self, obj):
        data = super(ClienteSerializer, self).to_representation(obj)  # the original data
        return data

    class Meta:
        model = Cliente
        fields = '__all__'