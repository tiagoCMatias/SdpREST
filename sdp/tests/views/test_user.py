from sdp.tests.TestSuite import TestSuit


class userTests(TestSuit):
    url_path = '/api/user/'

    def test_user_create(self):
        # Test Create
        # Empty Schema
        body = {}
        res = self.http_request('post', self.url_path, body)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json()['details'], 'Validation Error. Parameter username is a required property')

        #Test with numbers
        body = {
            'username': 1,
            'password': '123124',
            'email': '124125'
        }
        res = self.http_request('post', self.url_path, body)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json()['details'], 'Validation Error. 1 is not of type string. Review: username')

        # Test to pass
        username = "test_username"
        password = "test_password"
        email = "test_email"
        body = {
            'username': username,
            'password': password,
            'email': email
        }
        res = self.http_request('post', self.url_path, body)
        self.assertEqual(res.status_code, 200)

        # Test to fail - repeated email
        body = {
            'username': username,
            'password': password,
            'email': email
        }
        res = self.http_request('post', self.url_path, body)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json()['details'], 'Ocorreu um erro inesperado')

    def test_user_list(self):
        res = self.http_request('get', self.url_path)
        self.assertEqual(res.status_code, 405)

    def test_user_update(self):
        # Test Update
        # Empty Schema
        body = {}
        res = self.http_request('put', self.url_path+ '1/', body, auth_user='admin')
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json()['details'], 'Validation Error. Parameter username is a required property')

        # test to pass
        body = {
            'username': 'admin',
            'email': 'new@mail.com'
        }
        res = self.http_request('put', self.url_path + "1/", body, auth_user='admin')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()['details'], 'Utilizador actualizado')

        #Cant repeat usernames
        body = {
            'username': 'admin',
            'email': 'new@mail.com'
        }
        res = self.http_request('put', self.url_path + "2/", body, auth_user='normal')
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json()['details'], 'No Repeated Usernames')

        #No permission
        body = {
            'username': 'admin',
            'email': 'new@mail.com'
        }
        res = self.http_request('put', self.url_path + "2/", body, auth_user='admin')
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json()['details'], 'No permissions')




    def test_user_delete(self):
        # Test Delete
        res = self.http_request('delete', self.url_path + "1/")
        self.assertEqual(res.status_code, 405)


