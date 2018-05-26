from sdp.models.estrutura.componentes.familiaComponentes import FamiliaComponentes

from rest_framework import viewsets
from sdp.serializers.componentes.familiaComponente import FamiliaComponentesSerializer
from SdpREST.helpers.HttpException import HttpException
from SdpREST.helpers.HttpResponseHandler import HTTP
from SdpREST.helpers.SchemaValidator import SchemaValidator


class FamiliaComponentesViewModel(viewsets.GenericViewSet):

    @staticmethod
    def list(self):
        try:
            queryset = FamiliaComponentes.objects.all()
            data = FamiliaComponentesSerializer(queryset, many=True).to_representation(queryset)
        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            return HTTP.response(400, 'Some error occurred. {}. {}.'.format(type(e).__name__, str(e)))

        return HTTP.response(200, 'Familia de Componentes' ,data)

    @staticmethod
    def create(request):
        return HTTP.response(405, '')

    @staticmethod
    def update(request, pk=None):
        return HTTP.response(405, '')

    @staticmethod
    def destroy(request, pk=None):
        return HTTP.response(405, '')