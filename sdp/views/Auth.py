import bcrypt
import jwt

from django.conf import settings
from rest_framework import viewsets
from sdp.models.user import User

from SdpREST.helpers.HttpException import HttpException
from SdpREST.helpers.HttpResponseHandler import HTTP
from SdpREST.helpers.SchemaValidator import SchemaValidator


class AuthViewSet(viewsets.ModelViewSet):
    @staticmethod
    def login(request):
        try:
            #Check for Schema
            SchemaValidator.validate_obj_structure(request.data, 'login.json')
            # 1. Check if pair username-password is correct
            user = User.objects.filter(username=request.data['username'].lower()).get()
            if not bcrypt.checkpw(request.data['password'].encode('utf8'), user.password.encode('utf8')):
                raise HttpException(401, 'Credenciais não válidas.')
            # 4. Generate JWT
            jwt_data = {
                'user_id': user.id,
                'level_id': user.level.id,
            }
            jwt_encoded = jwt.encode(jwt_data, settings.JWT_SECRET,
                                     algorithm=settings.JWT_ALGORITHM).decode('utf-8')
            # Send Response
            data = {
                'jwt': jwt_encoded,
                'username': user.username,
                'level_id': user.level.id,
            }

            return HTTP.response(200, data=data)

        except User.DoesNotExist as e:
            return HTTP.response(401, 'Utilizador não existe.', 'User not valid.')
        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            return HTTP.response(400, 'Ocorreu um erro inesperado',
                                 'Unexpected Error. {}. {}.'.format(type(e).__name__, str(e)))

    @staticmethod
    def verify(request):
        try:
            #Check for Schema
            SchemaValidator.validate_obj_structure(request.data, 'login.json')
            # 1. Check if pair username-password is correct
            user = User.objects.filter(username=request.data['username'].lower()).get()
            if not bcrypt.checkpw(request.data['password'].encode('utf8'), user.password.encode('utf8')):
                raise HTTP.response(200, details=False)

            return HTTP.response(200, details=True)

        except User.DoesNotExist as e:
            return HTTP.response(200, details=False)
        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            return HTTP.response(400, 'Ocorreu um erro inesperado',
                                 'Unexpected Error. {}. {}.'.format(type(e).__name__, str(e)))
