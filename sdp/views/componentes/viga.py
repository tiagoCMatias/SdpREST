from sdp.models.estrutura.componentes.Viga.viga import Viga
from rest_framework import viewsets
from sdp.models.estrutura.componentes.Viga import vigaConfig
from sdp.models.configTenda import ConfigTenda

from SdpREST.helpers.SchemaValidator import SchemaValidator
from SdpREST.helpers.HttpException import HttpException
from SdpREST.helpers.HttpResponseHandler import HTTP

class VigaViewModel(viewsets.ModelViewSet):

    def list(self, request):
        return HTTP.response(200, "Nice try")

    @staticmethod
    def create(request):
        try:
            data = request.data
            print("Here")
            # 1. Check schema
            SchemaValidator.validate_obj_structure(data, 'componentes/viga.json')

            # 2. Add new User
            new_viga = Viga(
                nome=data['nome'] if 'nome' in data else None,
                tag=data['tag'] if 'tag' in data else None,
                descricao=data['descricao'] if 'descricao' in data else None,
            )
            new_viga.save()
            # 3. Create new Association
            for config_id in data['tipo']:
                tipo_Tenda = ConfigTenda.objects.get(pk=config_id)
                vigaConfig(
                    viga=new_viga,
                    tipoConfig=tipo_Tenda
                ).save()

            #new_vigaConfig.save()

            # 6. Generate Task Plan - TODO
            # TODO
        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            return HTTP.response(400, str(e))

        # Send Response
        return HTTP.response(200, 'Nova Viga')
