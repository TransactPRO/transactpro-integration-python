__author__ = 'olga'

import hashlib
from unittest import TestCase
from lib.gateclient import GateClient

class testGateClient(TestCase):

    init_data = {
            'rs': 'AAAA',
            'merchant_transaction_id': '1234567890',
            'user_ip': '127.0.0.1',
            'description': 'Test description',
            'amount': '1000',
            'currency': 'USD',
            'name_on_card': 'Vasyly Pupkin',
            'street': 'Main street 1',
            'zip': 'LV-0000',
            'city': 'Riga',
            'country': 'LV',
            'state': 'California',
            'email': 'email@example.lv',
            'phone': '+371 11111111',
            'card_bin': '511111',
            'bin_name': 'BANK',
            'bin_phone': '+371 11111111',
            'merchant_site_url': 'https://example.com'}

    sucsessful_response = 'OK:123'
    unsucsessful_response = 'ERROR:123'

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