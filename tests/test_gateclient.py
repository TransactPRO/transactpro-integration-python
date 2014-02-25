__author__ = 'olga'

import hashlib
from unittest import TestCase
from lib.gateclient import GateClient

class testGateClient(TestCase):

    def setUp(self):
        self.gate_client = GateClient('https://www.payment-api.com', 'AAAA-AAAA-AAAA-AAAA', '111')

    def test_constructor_check_url_success(self):
        self.assertEquals(self.gate_client.access_data['apiUrl'], 'https://www.payment-api.com')

    def test_constructor_check_guid_success(self):
        self.assertEquals(self.gate_client.access_data['guid'], 'AAAA-AAAA-AAAA-AAAA')

    def test_constructor_check_pass_success(self):
        password = hashlib.sha1('111')
        self.assertEquals(self.gate_client.access_data['pwd'], password.hexdigest())

    def test_constructor_check_verifySSL_success(self):
        self.assertTrue(self.gate_client.access_data['verifySSL'])