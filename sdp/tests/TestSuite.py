import json

from django.test import TestCase, Client
from rest_framework.test import APIClient

from sdp.models.userLevel import UserLevel
from sdp.models.user import User

class TestSuit(TestCase):
    fixtures = (
        '1tipoTendas.json',
        '2configTendas.json',
        '3familiaComponentes.json',
        '4userLevels.json',
        '5defaultUsers.json'
    )

    def setUp(self):
        self.client = Client()

        self.admin_role = UserLevel.objects.get(pk=1)
        self.normal_role = UserLevel.objects.get(pk=2)
        self.viewer_role = UserLevel.objects.get(pk=3)

        self.admin_user = User.objects.get(pk=1)
        self.normal_user = User.objects.get(pk=2)
        self.view_user = User.objects.get(pk=3)

        self.admin_jwt = self.get_jwt_from_login(username='admin', password='admin')
        self.normal_user = self.get_jwt_from_login(username='normal', password='normal')
        self.view_user = self.get_jwt_from_login(username='view', password='view')

    def get_jwt_from_login(self, username, password):
        headers = {'HTTP_PLATFORM': 'web'}
        url = '/api/login/'
        body = {'username': username, 'password': password}

        return self.client.post(url, json.dumps(body), **headers, format='json',
                                content_type='application/json').json()['data']['jwt']

    def http_request(self, method, url, body=None, auth_user=None, custom_headers=None, platform='web'):
        if not url.endswith('/'):
            url += '/'

        headers = {'HTTP_PLATFORM': platform}
        #if auth_user in ('admin', 'Admin') or auth_user is None:
        #    headers = {**headers, 'HTTP_JWT': self.admin_jwt}
        #elif auth_user in ('normal', 'Normal'):
        #    headers = {**headers, 'HTTP_JWT': self.doctor_jwt}

        #if custom_headers is not None:
        #    headers = {**headers, **custom_headers}

        if body is None:
            body = dict()

        client = APIClient()

        if method == 'get' or method == 'GET':
            response = client.get(url, **headers)
        elif method == 'post' or method == 'POST':
            response = self.client.post(url, json.dumps(body), **headers, format='json',
                                        content_type='application/json')
        elif method == 'put' or method == 'PUT':
            response = self.client.put(url, json.dumps(body), **headers, format='json', content_type='application/json')
        elif method == 'delete' or method == 'DELETE':
            response = self.client.delete(url, json.dumps(body), **headers, format='json',
                                          content_type='application/json')
        else:
            response = None

        return response
