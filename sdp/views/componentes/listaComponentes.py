import random
import string
from rest_framework import viewsets

from sdp.models.Componentes.componente import Componente
from sdp.models.Componentes.ListaDeComponentes import ListaDeComponentes
from SdpREST.helpers.HttpResponseHandler import HTTP
from SdpREST.helpers.SchemaValidator import SchemaValidator
from SdpREST.helpers.HttpException import HttpException

from sdp.serializers.componentes.listaDeComponentes import ListaDeComponentesSerializer
from sdp.serializers.componentes.componentes import ComponenteFamiliaSerializer

def checkList(data):
    for item in data:
        if (Componente.objects.check_item(item['componente']) == False):
            return False
    return True

def getItem(itemId):
    componente = Componente.objects.filter(id=itemId)
    return ComponenteFamiliaSerializer(componente, many=True).to_representation(componente)


class ListaComponentesViewSet(viewsets.GenericViewSet):

    @staticmethod
    def createList(request):
        data = request.data

        # 1. Check schema
        SchemaValidator.validate_obj_structure(data, 'componentes/listaDeComponentes.json')

        try:
            if checkList(data) is False:
                return HTTP.response(400, 'Wrong List')

            listCode = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

            for item in data:
                novoItem = ListaDeComponentes(
                    componente=Componente.objects.get(pk=item['componente']),
                    quantidade=item['quantidade'] if 'quantidade' in item else None,
                    codigoLista=listCode
                )
                novoItem.save()

            data = {
                "message": "Nova lista criada",
                "code": listCode
            }

        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)

        except Exception as e:
            return HTTP.response(400, 'Some error occurred. {}. {}.'.format(type(e).__name__, str(e)))

        return HTTP.response(200, data=data)

    @staticmethod
    def getItemList(request):
        data = request.data

        # 1. Check schema
        SchemaValidator.validate_obj_structure(data, 'componentes/listaDeComponentes.json')

        lista = []

        try:
            for index, item in enumerate(data):
                componente = getItem(item['componente'])
                print(componente[0])
                lista.append({'listNumber': index ,'Nome': componente[0]['nome'], 'Familia': componente[0]['familia']})

            data = {
                "message": "Sucess",
                "lista": lista
            }

        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)

        except Exception as e:
            return HTTP.response(400, 'Some error occurred. {}. {}.'.format(type(e).__name__, str(e)))

        return HTTP.response(200, data=data)


    @staticmethod
    def retrieve(request, pk=None):

        try:
            lista = ListaDeComponentes.objects.filter(codigoLista=pk)

            data = ListaDeComponentesSerializer(lista, many=True).to_representation(lista)

        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)

        except Exception as e:
            return HTTP.response(400, 'Some error occurred. {}. {}.'.format(type(e).__name__, str(e)))

        return HTTP.response(200, data=data)

    @staticmethod
    def create(request, pk=None):
        return HTTP.response(405, '')

    @staticmethod
    def update(request, pk=None):
        return HTTP.response(405, '')

    @staticmethod
    def destroy(request, pk=None):
        return HTTP.response(405, '')

