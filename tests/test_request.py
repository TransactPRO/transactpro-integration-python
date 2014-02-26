from unittest import TestCase
from mock import patch
from lib.request import Request

import pycurl
import lib.response as response


class TestRequest(TestCase):
    @patch('lib.request.StringIO.StringIO')
    @patch('lib.request.pycurl.Curl')
    def test_request_no_ssl(self, curl_mock, string_mock):
        curl_class = curl_mock.return_value
        curl_class.setopt.return_value = True
        string_class = string_mock.return_value
        string_class.write.return_value = None
        req = Request('http://example.com/', False)
        resp = req.executeRequest('init', {})
        curl_class.setopt.assert_called_with(pycurl.WRITEFUNCTION, string_class.write)
        self.assertEquals(curl_class.setopt.call_count, 7)

    @patch('lib.request.StringIO.StringIO')
    @patch('lib.request.pycurl.Curl')
    def test_request_with_ssl(self, curl_mock, string_mock):
        curl_class = curl_mock.return_value
        curl_class.setopt.return_value = True
        curl_class.perform.return_value = None
        string_class = string_mock.return_value
        string_class.write.return_value = None
        req = Request('http://example.com/', True)
        resp = req.executeRequest('init', {})
        curl_class.setopt.assert_called_with(pycurl.WRITEFUNCTION, string_class.write)
        curl_class.perform.assert_called_once()
        self.assertEquals(curl_class.setopt.call_count, 9)

    @patch('lib.request.StringIO.StringIO')
    @patch('lib.request.pycurl.Curl')
    def test_request_response_failure(self, curl_mock, string_mock):
        curl_class = curl_mock.return_value
        curl_class.setopt.return_value = True
        curl_class.perform.return_value = None
        string_class = string_mock.return_value
        string_class.write.return_value = None
        string_class.getvalue.return_value = ""
        curl_class.errstr.return_value = "Testing for error"

        req = Request('http://example.com/', False)
        resp = req.executeRequest('init', {})

        self.assertFalse(resp.is_success())
        self.assertEquals(resp.get_status(), response.FAILURE)
        self.assertEquals(resp.get_content(), "Testing for error")

    @patch('lib.request.StringIO.StringIO')
    @patch('lib.request.pycurl.Curl')
    def test_request_response_success(self, curl_mock, string_mock):
        curl_class = curl_mock.return_value
        curl_class.setopt.return_value = True
        curl_class.perform.return_value = None
        string_class = string_mock.return_value
        string_class.write.return_value = None
        string_class.getvalue.return_value = "Successful result"

        req = Request('http://example.com/', False)
        resp = req.executeRequest('init', {})

        self.assertTrue(resp.is_success())
        self.assertEquals(resp.get_status(), response.SUCCESS)
        self.assertEquals(resp.get_content(), "Successful result")

    @patch('lib.request.StringIO.StringIO')
    @patch('lib.request.pycurl.Curl')
    def test_request_verify_url_init(self, curl_mock, string_mock):
        curl_class = curl_mock.return_value
        string_class = string_mock.return_value
        string_class.getvalue.return_value = "Successful result"

        req = Request('http://example.com', False)
        resp = req.executeRequest('init', {})
        self.assertEquals(req.action_url, 'http://example.com/gwprocessor2.php?a=init')

    @patch('lib.request.StringIO.StringIO')
    @patch('lib.request.pycurl.Curl')
    def test_request_verify_url_charge(self, curl_mock, string_mock):
        curl_class = curl_mock.return_value
        string_class = string_mock.return_value
        string_class.getvalue.return_value = "Successful result"

        req = Request('http://example.com', False)
        resp = req.executeRequest('charge', {})
        self.assertEquals(req.action_url, 'http://example.com/gwprocessor2.php?a=charge')