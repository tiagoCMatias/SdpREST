from sdp.models.CRM.cliente import Cliente
from django.test import TestCase
from SdpREST.helpers.HttpException import HttpException
from sdp.tests.TestSuite import TestSuit


class crmClientTests(TestSuit):
    url_path = '/api/crm/clientes/'

    def test_cliente_create(self):
        # Test Create
        res = self.http_request('post', self.url_path)
        self.assertEqual(res.status_code, 405)

    def test_cliente_list(self):
        res = self.http_request('get', self.url_path)
        self.assertEqual(res.status_code, 200)

    def test_update_cliente(self):
        # Test Update
        res = self.http_request('put', self.url_path )
        self.assertEqual(res.status_code, 405)

    def test_cliente_delete(self):
        # Test Delete
        res = self.http_request('delete', self.url_path)
        self.assertEqual(res.status_code, 405)
