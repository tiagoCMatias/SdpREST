from rest_framework.viewsets import GenericViewSet
from SdpREST.helpers.HttpResponseHandler import HTTP

import bcrypt


from SdpREST.helpers.HttpException import HttpException
from SdpREST.helpers.SchemaValidator import SchemaValidator
from sdp.models.userLevel import UserLevel
from sdp.models.user import User


class UserViewSet(GenericViewSet):

    @staticmethod
    def create(request):
        try:
            data = request.data
            # 1.2. Check schema
            SchemaValidator.validate_obj_structure(request.data, 'createUser.json')
            user = User(
                email=data['email'].lower() if 'email' in data else None,
                username=data['username'].lower() if 'username' in data else None,
                level=
                    UserLevel.objects.filter(pk=request.data['level']).get()
                    if 'level' in data
                    else UserLevel.objects.viewer_level().get(),
                password=str(bcrypt.hashpw(request.data['password'].encode('utf8'), bcrypt.gensalt()), 'utf8'),
            )
            user.save()

        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            return HTTP.response(400,
                                 'Ocorreu um erro inesperado',
                                 'Unexpected Error. {}. {}.'.format(type(e).__name__, str(e)))

        return HTTP.response(200, 'Utilizador criado com sucesso.')

    @staticmethod
    def list(self):
        return HTTP.response(405, '')

    @staticmethod
    def update(request, pk=None):
        return HTTP.response(405, '')

    @staticmethod
    def destroy(request, pk=None):
        return HTTP.response(405, '')