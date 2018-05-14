from rest_framework.viewsets import GenericViewSet
from SdpREST.helpers.HttpException import HttpException
from SdpREST.helpers.HttpResponseHandler import HTTP
from SdpREST.helpers.SchemaValidator import SchemaValidator
from sdp.models import tipoTendas as TipoTenda
from sdp.serializers.tipoTenda import TipoTendaSerializer

class TipoTendasViewSet(GenericViewSet):
    def list(self, request):
        try:
            print(TipoTenda.objects.all())
            tipoTenda = self.paginate_queryset(TipoTenda.objects.all())
            #queryset = self.paginate_queryset(tipoTenda)

        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            print(e)
            return HTTP.response(400, 'Some error occurred. {}. {}.'.format(type(e).__name__, str(e)))

        data = TipoTendaSerializer(tipoTenda, many=True).data

        return HTTP.response(200, '', data=data, paginator=self.paginator)

    @staticmethod
    def create(request):
        return HTTP.response(405, '')

    @staticmethod
    def update(request, pk=None):
        return HTTP.response(405, '')

    @staticmethod
    def destroy(request, pk=None):
        return HTTP.response(405, '')
