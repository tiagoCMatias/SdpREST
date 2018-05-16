from rest_framework.decorators import list_route
from rest_framework.viewsets import GenericViewSet
from SdpREST.helpers.HttpResponseHandler import HTTP

from SdpREST.helpers.HttpException import HttpException
from sdp.models.user import User


class UserViewSet(GenericViewSet):
    @staticmethod
    @list_route(methods=['post'])
    def activate(request):
        try:
            if 'password' not in request.data:
                raise HttpException(400, 'You need to send password')

            user = User.objects.filter(email=request.data['email']).get()
            if user.is_active:
                raise HttpException(400, 'email already in use.')

            user.password = request.data['password']
            user.save()

        except User.DoesNotExist:
            return HTTP.response(404, 'Invalid Activation Code.')
        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            return HTTP.response(400, 'Some error occurred. {}. {}.'.format(type(e).__name__, str(e)))

        return HTTP.response(200, 'User Created.')
