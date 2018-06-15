from sdp.models.tendas.configTenda import ConfigTenda
from rest_framework import viewsets
from sdp.serializers.tendas.configTenda import ConfigTendaSerializer

from SdpREST.helpers.HttpException import HttpException
from SdpREST.helpers.HttpResponseHandler import HTTP
from SdpREST.helpers.SchemaValidator import SchemaValidator

class ConfigTendaViewSet(viewsets.GenericViewSet):

    @staticmethod
    def list(self, request):
        try:
            queryset = ConfigTenda.objects.all()
            data = ConfigTendaSerializer(queryset, many=True).to_representation(queryset)

        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            return HTTP.response(400, 'Some error occurred. {}. {}.'.format(type(e).__name__, str(e)))

        return HTTP.response(200, 'Configurações de Tendas' ,data)

    @staticmethod
    def create(request):
        return HTTP.response(405, '')

    @staticmethod
    def update(request, pk=None):
        return HTTP.response(405, '')

    @staticmethod
    def destroy(request, pk=None):
        return HTTP.response(405, '')
