from rest_framework.viewsets import GenericViewSet
from SdpREST.helpers.HttpException import HttpException
from SdpREST.helpers.HttpResponseHandler import HTTP
from sdp.models.tendas.tipoTendas import TipoTenda
from sdp.serializers.tendas.tipoTenda import TipoTendaSerializer

class TipoTendasViewSet(GenericViewSet):

    @staticmethod
    def list(self):
        try:
            queryset = TipoTenda.objects.all()
            data = TipoTendaSerializer(queryset, many=True).to_representation(queryset)

        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            return HTTP.response(400,
                                 'Ocorreu um erro inesperado',
                                 'Unexpected Error. {}. {}.'.format(type(e).__name__, str(e)))

        return HTTP.response(200, 'Tipo de Tendas', data)

    @staticmethod
    def create(request):
        return HTTP.response(405, details='No Access')

    @staticmethod
    def update(request, pk=None):
        return HTTP.response(405, details='No Access')

    @staticmethod
    def delete(request, pk=None):
        return HTTP.response(405, details='No Access')
