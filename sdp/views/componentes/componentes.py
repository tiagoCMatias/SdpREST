# Models
from sdp.models.estrutura.componentes.componente import Componente
from sdp.models.estrutura.componentes.familiaComponentes import FamiliaComponentes
from sdp.models.tendas.configTenda import ConfigTenda
from sdp.models.estrutura.listaComponentes import ListaDeComponentes
from rest_framework import viewsets
from sdp.serializers.componentes.componentes import ComponentesSerializer, FullComponentesSerializer
from sdp.serializers.componentes.listaComponentes import ListaDeComponentesSerializer
from SdpREST.helpers.HttpException import HttpException
from SdpREST.helpers.HttpResponseHandler import HTTP
from SdpREST.helpers.SchemaValidator import SchemaValidator

from collections import OrderedDict
import json


class ComponentesViewModel(viewsets.GenericViewSet):

    @staticmethod
    def list(self):
        try:
            queryset = Componente.objects.all()
            data = FullComponentesSerializer(queryset, many=True).to_representation(queryset)

            # data = []
            #
            # for component in components:
            #     queryset = ListaDeComponentes.objects.filter(componente=component['id']).all()
            #     pertence = ListaDeComponentesSerializer(queryset, many=True).to_representation(queryset)
            #
            #     data.append({
            #         'id': component['id'],
            #         'nome': component['nome'],
            #         'descricao': component['descricao'],
            #         'quantidade': component['quantidade'],
            #         'genCodigo': component['genCodigo'],
            #         'familia': component['familia'],
            #         'pertence': pertence
            #     })

        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            return HTTP.response(400, 'Some error occurred. {}. {}.'.format(type(e).__name__, str(e)))

        return HTTP.response(200, 'Familia de Componentes', data)

    @staticmethod
    def create(request):
        try:
            data = request.data
            # 1. Check schema
            SchemaValidator.validate_obj_structure(data, 'componentes/componentes.json')

            # 2. Validate
            if (FamiliaComponentes.objects.familia_exist(data['familia']) == False):
                return HTTP.response(400, 'Validation Error. Parameter Familia is wrong')

            familia = FamiliaComponentes.objects.get(pk=data['familia'])
            genCodigo = Componente.objects.count_familia(data['familia']) + 1

            genCodigo = str(familia.id) + '.' + str(genCodigo)

            novoComponente = Componente(
                nome=data['nome'] if 'nome' in data else None,
                descricao=data['descricao'] if 'descricao' in data else None,
                tag=data['tag'] if 'tag' in data else None,
                quantidade=data['quantidade'] if 'quantidade' in data else None,
                familia=familia,
                genCodigo=genCodigo
            )
            novoComponente.save()

            lista_de_components_to_save = list()
            for tenda_id in data['tenda']:
                tipoTenda = ConfigTenda.objects.get(pk=tenda_id)
                lista_de_components_to_save.append(ListaDeComponentes(
                    componente=novoComponente,
                    tenda=tipoTenda
                ))
            ListaDeComponentes.objects.bulk_create(lista_de_components_to_save)


        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            return HTTP.response(400, 'Some error occurred. {}. {}.'.format(type(e).__name__, str(e)))

        return HTTP.response(200, 'Novo Componente Registado')

    @staticmethod
    def update(request, pk=None):
        return HTTP.response(405, '')

    @staticmethod
    def destroy(request, pk=None):
        return HTTP.response(405, '')

