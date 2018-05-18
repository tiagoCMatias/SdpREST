from rest_framework import serializers

from sdp.models.estrutura.componentes.familiaComponentes import FamiliaComponentes


class FamiliaComponentesSerializer(serializers.ModelSerializer):

    def to_representation(self, obj):
        data = super(FamiliaComponentesSerializer, self).to_representation(obj)  # the original data
        return data

    class Meta:
        model = FamiliaComponentes
        fields = '__all__'