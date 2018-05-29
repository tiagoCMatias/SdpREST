from sdp.tests.TestSuite import TestSuit


class tipoTendasTests(TestSuit):
    url_path = '/api/tendas/tipos/'

    def test_tipo_create(self):
        # Test Create
        res = self.http_request('post', self.url_path + "1/")
        self.assertEqual(res.status_code, 405)

    def test_tipo_list(self):
        res = self.http_request('get', self.url_path)
        self.assertEqual(res.status_code, 200)

    def test_tipo_update(self):
        # Test Update
        res = self.http_request('put', self.url_path + "1/")
        self.assertEqual(res.status_code, 405)


    def test_tipo_delete(self):
        # Test Delete
        res = self.http_request('delete', self.url_path + "1/")
        self.assertEqual(res.status_code, 405)
