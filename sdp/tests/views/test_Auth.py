from sdp.tests.TestSuite import TestSuit


class tipoTendasTests(TestSuit):
    url_path = '/api/login/'

    def test_login(self):
        # Test Create
        # Empty Schema
        body = {}
        res = self.http_request('post', self.url_path, body)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json()['details'], 'Validation Error. Parameter username is a required property')

        body = {
            "username": "username",
        }
        res = self.http_request('post', self.url_path, body)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json()['details'], 'Validation Error. Parameter password is a required property')

        #Test to pass
        admin_auth = "admin"
        body = {
            "username": "admin",
            "password": admin_auth
        }
        res = self.http_request('post', self.url_path, body)
        self.assertEqual(res.status_code, 200)


