from sdp.tests.TestSuite import TestSuit


class userTests(TestSuit):
    url_path = '/api/user/'

    def test_user_create(self):
        # Test Create
        res = self.http_request('post', self.url_path)
        self.assertEqual(res.status_code, 405)

    def test_user_list(self):
        res = self.http_request('post', self.url_path)
        self.assertEqual(res.status_code, 405)

    def test_user_cliente(self):
        # Test Update
        res = self.http_request('put', self.url_path )
        self.assertEqual(res.status_code, 405)

    def test_user_delete(self):
        # Test Delete
        res = self.http_request('delete', self.url_path)
        self.assertEqual(res.status_code, 405)
