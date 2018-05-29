from sdp.tests.TestSuite import TestSuit


class crmClientTests(TestSuit):
    url_path = '/api/crm/obra/'

    valid_date = '2003-12-23'
    invalid_date = '2003-12-32'

    def test_obra_create(self):
        # Test Create
        # Empty Schema
        body = {}
        res = self.http_request('post', self.url_path, body)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json()['details'], 'Validation Error. Parameter local is a required property')

        #Test bad date
        body = {
            'local': 'localTeste',
            'cliente': 'ClienteTeste',
            'data': self.invalid_date
        }
        res = self.http_request('post', self.url_path, body)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(res.json()['details'], 'Incorrect data format, should be YYYY-MM-DD')

        # Test to pass with new Cliente
        body = {
            'local': 'localTeste',
            'cliente': 'ClienteTeste',
            'data': self.valid_date
        }
        res = self.http_request('post', self.url_path, body)
        self.assertEqual(res.status_code, 200)

        # Test with the same Cliente
        body = {
            'local': 'localTeste',
            'cliente': 'ClienteTeste',
            'data': self.valid_date
        }
        res = self.http_request('post', self.url_path, body)
        self.assertEqual(res.status_code, 200)


    def test_obra_list(self):
        res = self.http_request('get', self.url_path)
        self.assertEqual(res.status_code, 200)

    def test_obra_cliente(self):
        # Test Update
        res = self.http_request('put', self.url_path + "1/")
        self.assertEqual(res.status_code, 405)

    def test_obra_delete(self):
        # Test Delete
        res = self.http_request('delete', self.url_path + "1/")
        self.assertEqual(res.status_code, 405)