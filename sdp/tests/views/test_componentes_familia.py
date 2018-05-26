from sdp.tests.TestSuite import TestSuit


class componentesFamiliaTests(TestSuit):
    url_path = '/api/componentes/familia/'

    def test_familia_create(self):
        # Test Create
        res = self.http_request('post', self.url_path)
        self.assertEqual(res.status_code, 405)

    def test_familia_list(self):
        # Test list
        res = self.http_request('get', self.url_path)
        self.assertEqual(res.status_code, 200)

    def test_familia_update(self):
        # Test Update
        res = self.http_request('put', self.url_path )
        self.assertEqual(res.status_code, 405)

    def test_familia_delete(self):
        # Test Delete
        res = self.http_request('delete', self.url_path)
        self.assertEqual(res.status_code, 405)
