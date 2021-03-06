import json

from django.test import TestCase

from SdpREST.helpers.HttpResponseHandler import HTTP


class HttpResponseHandlerTest(TestCase):
    def test_code_message_responses(self):
        res = HTTP.response(200)
        body = json.loads(res.content)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['code'], 200)
        self.assertEqual(body['message'], 'Success')
        self.assertEqual(body['details'], '')
        self.assertEqual(body['data'], {})

        res = HTTP.response(201)
        body = json.loads(res.content)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(body['code'], 201)
        self.assertEqual(body['message'], 'Created')
        self.assertEqual(body['details'], '')
        self.assertEqual(body['data'], {})

        res = HTTP.response(202)
        body = json.loads(res.content)
        self.assertEqual(res.status_code, 202)
        self.assertEqual(body['code'], 202)
        self.assertEqual(body['message'], 'Accepted')
        self.assertEqual(body['details'], '')
        self.assertEqual(body['data'], {})

        res = HTTP.response(204)
        body = json.loads(res.content)
        self.assertEqual(res.status_code, 204)
        self.assertEqual(body['code'], 204)
        self.assertEqual(body['message'], 'No content')
        self.assertEqual(body['details'], '')
        self.assertEqual(body['data'], {})

        res = HTTP.response(400)
        body = json.loads(res.content)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(body['code'], 400)
        self.assertEqual(body['message'], 'Bad request')
        self.assertEqual(body['details'], '')
        self.assertEqual(body['data'], {})

        res = HTTP.response(401)
        body = json.loads(res.content)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(body['code'], 401)
        self.assertEqual(body['message'], 'Unauthorized')
        self.assertEqual(body['details'], '')
        self.assertEqual(body['data'], {})

        res = HTTP.response(403)
        body = json.loads(res.content)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(body['code'], 403)
        self.assertEqual(body['message'], 'Forbidden')
        self.assertEqual(body['details'], '')
        self.assertEqual(body['data'], {})

        res = HTTP.response(404)
        body = json.loads(res.content)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(body['code'], 404)
        self.assertEqual(body['message'], 'Not found')
        self.assertEqual(body['details'], '')
        self.assertEqual(body['data'], {})

        res = HTTP.response(405)
        body = json.loads(res.content)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(body['code'], 405)
        self.assertEqual(body['message'], 'Method not allowed')
        self.assertEqual(body['details'], '')
        self.assertEqual(body['data'], {})

        res = HTTP.response(500)
        body = json.loads(res.content)
        self.assertEqual(res.status_code, 500)
        self.assertEqual(body['code'], 500)
        self.assertEqual(body['message'], 'Internal error')
        self.assertEqual(body['details'], '')
        self.assertEqual(body['data'], {})

        res = HTTP.response(501)
        body = json.loads(res.content)
        self.assertEqual(res.status_code, 501)
        self.assertEqual(body['code'], 501)
        self.assertEqual(body['message'], 'Not Implemented')
        self.assertEqual(body['details'], '')
        self.assertEqual(body['data'], {})

    def test_details_in_responses(self):
        res = HTTP.response(200, 'This is a test for details')
        body = json.loads(res.content)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['code'], 200)
        self.assertEqual(body['message'], 'Success')
        self.assertEqual(body['details'], 'This is a test for details')
        self.assertEqual(body['data'], {})

    def test_data_in_responses(self):
        res = HTTP.response(200, 'This is a test for details', {'foo': 'bar', 'test': 'success'})
        body = json.loads(res.content)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(body['code'], 200)
        self.assertEqual(body['message'], 'Success')
        self.assertEqual(body['details'], 'This is a test for details')
        self.assertEqual(body['data']['foo'], 'bar')
        self.assertEqual(body['data']['test'], 'success')
