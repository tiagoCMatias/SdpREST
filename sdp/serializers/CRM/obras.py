#from datetime import datetime
from rest_framework import serializers

from sdp.models.CRM.obras import Obras
from sdp.models.CRM.cliente import Cliente

class ObrasSerializer(serializers.ModelSerializer):

    def to_representation(self, obj):
        data = super(ObrasSerializer, self).to_representation(obj)  # the original data
        data['cliente'] = Cliente.objects.get_nome(id=data['cliente']).nome
        #data['date'] = datetime.strptime(data['date'], '%Y-%m-%d').strftime('%Y-%m-%d')
        return data

    class Meta:
        model = Obras
        fields = '__all__'