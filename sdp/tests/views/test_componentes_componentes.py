from sdp.tests.TestSuite import TestSuit
from django.db import transaction


class componentesCompTests(TestSuit):
    url_path = '/api/componentes/lista/'

    def test_componentes_create(self):
        # Test Create
        # Empty Schema
        body = {}
        res = self.http_request('post', self.url_path, body)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json()['details'], 'Validation Error. Parameter nome is a required property')

        # Wrong Familia
        body = {
            'nome': 'nome',
            'descricao': 'descricao',
            'tag': 'tag',
            'quantidade': 1,
            'familia': 99,
            'tenda': [1, 2]
        }
        res = self.http_request('post', self.url_path, body)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json()['details'], 'Validation Error. Parameter Familia is wrong')

        # Test to pass
        new_tag = 'new_tag'
        body = {
            'nome': 'nome',
            'descricao': 'descricao',
            'tag': new_tag,
            'quantidade': 1,
            'familia': 1,
            'tenda': [3, 4]
        }
        res = self.http_request('post', self.url_path, body)
        self.assertEqual(res.status_code, 200)

        # Wrong Tenda
        repeated_tag = 'tag'
        body = {
            'nome': 'nome',
            'descricao': 'descricao',
            'tag': repeated_tag,
            'quantidade': 1,
            'familia': 1,
            'tenda': [98, 99]
        }
        res = self.http_request('post', self.url_path, body)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json()['details'],
                         'Some error occurred. DoesNotExist. ConfigTenda matching query does not exist..')

        # Test to repeated tag
        body = {
            'nome': 'nome',
            'descricao': 'descricao',
            'tag': repeated_tag,
            'quantidade': 1,
            'familia': 1,
            'tenda': [99, 98]
        }
        res = self.http_request('post', self.url_path, body)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json()['details'],
                         'Some error occurred. IntegrityError. UNIQUE constraint failed: componentesEstrutura.tag.')


    def test_componentes_list(self):
        # Test list
        res = self.http_request('get', self.url_path)
        self.assertEqual(res.status_code, 200)

    def test_componentes_update(self):
        # Test Update
        res = self.http_request('put', self.url_path )
        self.assertEqual(res.status_code, 405)

    def test_componentes_delete(self):
        # Test Delete
        res = self.http_request('delete', self.url_path)
        self.assertEqual(res.status_code, 405)
