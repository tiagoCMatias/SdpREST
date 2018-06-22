# Models
from sdp.models.Componentes.componente import Componente
from sdp.models.Componentes.familiaComponentes import FamiliaComponentes
from sdp.models.Tendas.configTenda import ConfigTenda
from sdp.models.Componentes.familiaToComponente import FamiliaToComponentes
from rest_framework import viewsets
from sdp.serializers.componentes.componentes import FullComponentesSerializer
from SdpREST.helpers.HttpException import HttpException
from SdpREST.helpers.HttpResponseHandler import HTTP
from SdpREST.helpers.SchemaValidator import SchemaValidator


class ComponentesViewModel(viewsets.GenericViewSet):

    @staticmethod
    def list(self):
        try:
            queryset = Componente.objects.all()
            data = FullComponentesSerializer(queryset, many=True).to_representation(queryset)

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
                peso=data['peso'] if 'peso' in data else None,
                quantidade=data['quantidade'] if 'quantidade' in data else None,
                familia=familia,
                genCodigo=genCodigo
            )
            novoComponente.save()

            lista_de_components_to_save = list()
            for tenda_id in data['tenda']:
                tipoTenda = ConfigTenda.objects.get(pk=tenda_id)
                lista_de_components_to_save.append(FamiliaToComponentes(
                    componente=novoComponente,
                    tenda=tipoTenda
                ))
            FamiliaToComponentes.objects.bulk_create(lista_de_components_to_save)


        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            return HTTP.response(400, 'Some error occurred. {}. {}.'.format(type(e).__name__, str(e)))

        return HTTP.response(200, 'Novo Componente Registado')

    @staticmethod
    def update(request, pk=None):
        try:

            updateComponente = request.data
            # 1. Check schema
            SchemaValidator.validate_obj_structure(updateComponente, 'componentes/updateComponente.json')

            myComponente = Componente.objects.get(pk=pk)

            if updateComponente['familia']:
                familia = FamiliaComponentes.objects.get(pk=updateComponente['familia'])
                myComponente.familia = familia

            myComponente.nome = updateComponente['nome'] if 'nome' in updateComponente else myComponente.nome
            myComponente.descricao = updateComponente['descricao'] if 'descricao' in updateComponente else myComponente.descricao
            myComponente.quantidade = updateComponente['quantidade'] if 'quantidade' in updateComponente else myComponente.quantidade

            myComponente.save()

        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            return HTTP.response(400, 'Some error occurred. {}. {}.'.format(type(e).__name__, str(e)))

        return HTTP.response(200, 'Update Success')

    @staticmethod
    def destroy(request, pk=None):
        return HTTP.response(405, '')

