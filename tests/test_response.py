from unittest import TestCase
from transactpro.response import Response, SUCCESS, FAILURE


class TestResponse(TestCase):

    def test_response_successful(self):
        resp = Response(SUCCESS, "OK")
        self.assertEquals(resp.is_success(), SUCCESS)
        self.assertEquals(resp.get_status(), SUCCESS)
        self.assertEquals(resp.get_content(), "OK")

    def test_response_failed(self):
        resp = Response(FAILURE, "Error here")
        self.assertEquals(resp.is_success(), FAILURE)

    def test_get_formatted_content_failure(self):
        resp = Response(FAILURE, "Any error test")
        self.assertEquals(resp.get_formatted_content(), {})

    def test_get_formatted_content_success(self):
        resp = Response(SUCCESS, "id:13~result:success~ip:127.0.0.1")
        self.assertEquals(resp.get_formatted_content(), { 'id':'13', 'result':'success', 'ip':'127.0.0.1'})

    def test_get_formatted_content_empty(self):
        resp = Response(SUCCESS, "id:13~novaluekey")
        self.assertEquals(resp.get_formatted_content(), {'id':'13', 'novaluekey':''})

    def test_get_formatted_content_doublecolon(self):
        resp = Response(SUCCESS, "id:13~key:this:contains:double:colon")
        self.assertEquals(resp.get_formatted_content(), {'id':'13', 'key':'this:contains:double:colon'})