from sdp.models.CRM.cliente import Cliente
from rest_framework import viewsets
from sdp.serializers.CRM.cliente import ClienteSerializer

from SdpREST.helpers.HttpException import HttpException
from SdpREST.helpers.HttpResponseHandler import HTTP
from SdpREST.helpers.SchemaValidator import SchemaValidator


class ClienteViewModel(viewsets.ModelViewSet):

    @staticmethod
    def list(self):
        try:
            queryset = Cliente.objects.all()
            data = ClienteSerializer(queryset, many=True).to_representation(queryset)
        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            return HTTP.response(400, 'Some error occurred. {}. {}.'.format(type(e).__name__, str(e)))

        return HTTP.response(200, 'Lista de Clientes' ,data)