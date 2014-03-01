__author__ = 'olga'

import hashlib
from unittest import TestCase
from lib.gateclient import GateClient
from mock import patch, Mock

class TestGateClient(TestCase):

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

    @patch('lib.gateclient.Validator')
    @patch('lib.gateclient.Request')
    def test_init_request(self, req_mock, validator_mock):
        validator_class = Mock()
        validator_class.execute.return_value = {}
        validator_mock.return_value = validator_class

        req_class = Mock()
        req_class.executeRequest.return_value = None
        req_mock.return_value = req_class

        gate_client = GateClient('https://www.payment-api.com', 'AAAA-AAAA-AAAA-AAAA', '111')

        result_data = gate_client.init(self.init_data)
        expected_data = { 'guid': 'AAAA-AAAA-AAAA-AAAA', 'account_guid': 'AAAA-AAAA-AAAA-AAAA'}
        expected_data['pwd'] = hashlib.sha1('111').hexdigest()
        req_class.executeRequest.assert_called_once_with('init', expected_data)

    @patch('lib.gateclient.Request')
    def test_charge_request(self, req_mock):
        req_class = Mock()
        req_class.executeRequest.return_value = None
        req_mock.return_value = req_class

        gate_client = GateClient('https://www.payment-api.com', 'AAAA-AAAA-AAAA-AAAA', '111')

        initial_data = {'init_transaction_id': 1, 'cc': '1234123412341234', 'cvv': '666', 'expire': '12/13', 'f_extended': 5}
        result_data = gate_client.charge(initial_data)
        expected_data = initial_data
        expected_data['guid'] = 'AAAA-AAAA-AAAA-AAAA'
        expected_data['account_guid'] = 'AAAA-AAAA-AAAA-AAAA'
        expected_data['pwd'] = hashlib.sha1('111').hexdigest()
        req_class.executeRequest.assert_called_once_with('charge', expected_data)