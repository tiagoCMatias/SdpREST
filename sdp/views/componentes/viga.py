from sdp.models.componentes.Viga.viga import Viga
from rest_framework import viewsets
from sdp.serializers.componentes.viga import VigaSerializer
from sdp.models.componentes.Viga.vigaConfig import vigaConfig

from SdpREST.helpers.SchemaValidator import SchemaValidator
from SdpREST.helpers.HttpException import HttpException
from SdpREST.helpers.HttpResponseHandler import HTTP

class VigaViewModel(viewsets.ModelViewSet):
    @staticmethod
    def create(request):
        try:
            data = request.data
            # 1. Check schema
            SchemaValidator.validate_obj_structure(data, 'componentes/viga.json')

            # 2. Add new User
            new_viga = Viga(
                name=data['name'] if 'name' in data else None,
                tag=data['tag'] if 'tag' in data else None,
            )
            new_viga.save()
            # 3. Create new Association

            new_vigaConfig = vigaConfig(
                viga=new_viga.pk,
                tipoConfig=data['tipo'] if 'tipo' in data else None,
            )
            new_vigaConfig.save()

            # 6. Generate Task Plan - TODO
            # TODO
        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            return HTTP.response(400, str(e))

        # Send Response
        return HTTP.response(200, 'Nova Viga')
