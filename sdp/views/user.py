from rest_framework.decorators import list_route
from rest_framework.viewsets import GenericViewSet
from SdpREST.helpers.HttpResponseHandler import HTTP

from SdpREST.helpers.HttpException import HttpException
from sdp.models.user import User


class UserViewSet(GenericViewSet):
    @staticmethod
    def list(self):
        return HTTP.response(405, '')

    @staticmethod
    def create(request):
        return HTTP.response(405, '')

    @staticmethod
    def update(request, pk=None):
        return HTTP.response(405, '')

    @staticmethod
    def destroy(request, pk=None):
        return HTTP.response(405, '')