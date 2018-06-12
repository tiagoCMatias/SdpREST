import jwt
from jwt import DecodeError

from SdpREST.helpers.HttpResponseHandler import HTTP
from django.conf import settings


class SdpMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.path not in ('/api/login/', '/api/login'):
            if 'HTTP_JWT' not in request.META:
                return HTTP.response(401, 'Falta o token nos headers.', 'Token not present')

            try:
                jwt_encoded = request.META['HTTP_JWT']
                jwt_decoded = jwt.decode(jwt_encoded, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
            except jwt.ExpiredSignatureError:
                return HTTP.response(401, 'Token Expired', 'Token not valid.')
            except DecodeError:
                return HTTP.response(401, 'Token não é válido.', 'Token not valid.')

            request.USER_ID = jwt_decoded['user_id']
            request.LEVEL_ID = jwt_decoded['level_id']

        return self.get_response(request)
