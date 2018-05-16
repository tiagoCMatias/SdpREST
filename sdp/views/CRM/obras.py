from datetime import datetime

from rest_framework.viewsets import GenericViewSet

from SdpREST.helpers.HttpException import HttpException
from SdpREST.helpers.HttpResponseHandler import HTTP
from SdpREST.helpers.SchemaValidator import SchemaValidator

from sdp.models.CRM.cliente import Cliente
from sdp.models.CRM.obras import Obras

from sdp.serializers.CRM.obras import ObrasSerializer


class ObrasViewModel(GenericViewSet):

    @staticmethod
    def list(self):
        try:
            queryset = Obras.objects.all()
            data = ObrasSerializer(queryset, many=True).to_representation(queryset)
        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            return HTTP.response(400, 'Some error occurred. {}. {}.'.format(type(e).__name__, str(e)))

        return HTTP.response(200, 'Obras' ,data)


    @staticmethod
    def create(request):
        try:
            data = request.data
            # 1. Check schema
            SchemaValidator.validate_obj_structure(data, 'CRM/obras.json')

            # Check if Cliente exists
            cliente = Cliente.objects.match_cliente(nome=data['cliente'])

            if cliente:
                novaObra = Obras(
                    date=datetime.strptime(data['data'], '%Y-%m-%d'),
                    cliente=cliente,
                    local=data['local']
                )
                novaObra.save()
                message = "Nova obra adicionado"
            else:
                print("create new client")
                novoCliente = Cliente(
                    nome=data['cliente'],
                    descricao="Sem descricao"
                )
                novoCliente.save()

                novaObra = Obras(
                    date=datetime.strptime(data['data'], '%Y-%m-%d'),
                    cliente=novoCliente,
                    local=data['local']
                )
                novaObra.save()
                message = "Nova obra e cliente adicionado"

        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            return HTTP.response(400, 'Some error occurred. {}. {}.'.format(type(e).__name__, str(e)))

        return HTTP.response(200, message)

    @staticmethod
    def update(request, pk=None):
        return HTTP.response(405, '')

    @staticmethod
    def destroy(request, pk=None):
        return HTTP.response(405, '')
