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

    successful_response = 'OK:123'
    unsuccessful_response = 'ERROR:123'

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
        
    @patch('lib.gateclient.Request')
    def test_refund_request(self, req_mock):
        req_class = Mock()
        req_class.executeRequest.return_value = None
        req_mock.return_value = req_class

        gate_client = GateClient('https://www.payment-api.com', 'AAAA-AAAA-AAAA-AAAA', '111')

        initial_data = {'init_transaction_id': 1, 'amount_to_refund': 100}
        result_data = gate_client.refund(initial_data)
        expected_data = initial_data
        expected_data['pwd'] = hashlib.sha1('111').hexdigest()
        expected_data['guid'] = 'AAAA-AAAA-AAAA-AAAA'
        expected_data['account_guid'] = 'AAAA-AAAA-AAAA-AAAA'
        req_class.executeRequest.assert_called_once_with('refund', expected_data)

    @patch('lib.gateclient.Validator')
    @patch('lib.gateclient.Request')
    def test_init_dms_request(self, req_mock, validator_mock):
        validator_class = Mock()
        validator_class.execute.return_value = {}
        validator_mock.return_value = validator_class

        req_class = Mock()
        req_class.executeRequest.return_value = None
        req_mock.return_value = req_class

        gate_client = GateClient('https://www.payment-api.com', 'AAAA-AAAA-AAAA-AAAA', '111')

        result_data = gate_client.init_dms(self.init_data)
        expected_data = { 'guid': 'AAAA-AAAA-AAAA-AAAA', 'account_guid': 'AAAA-AAAA-AAAA-AAAA'}
        expected_data['pwd'] = hashlib.sha1('111').hexdigest()
        req_class.executeRequest.assert_called_once_with('init_dms', expected_data)

    @patch('lib.gateclient.Request')
    def test_make_hold_request(self, req_mock):
        req_class = Mock()
        req_class.executeRequest.return_value = None
        req_mock.return_value = req_class

        gate_client = GateClient('https://www.payment-api.com', 'AAAA-AAAA-AAAA-AAAA', '111')

        initial_data = {
            'f_extended': '5',
            'init_transaction_id': '121212',
            'cc': '00000000000000000',
            'cvv': '666',
            'expire': '01/17'}
        result_data = gate_client.make_hold(initial_data)
        expected_data = initial_data
        expected_data['guid'] = 'AAAA-AAAA-AAAA-AAAA'
        expected_data['account_guid'] = 'AAAA-AAAA-AAAA-AAAA'
        expected_data['pwd'] = hashlib.sha1('111').hexdigest()
        req_class.executeRequest.assert_called_once_with('make_hold', expected_data)

    @patch('lib.gateclient.Request')
    def test_charge_hold_request(self, req_mock):
        req_class = Mock()
        req_class.executeRequest.return_value = None
        req_mock.return_value = req_class

        gate_client = GateClient('https://www.payment-api.com', 'AAAA-AAAA-AAAA-AAAA', '111')

        initial_data = {'init_transaction_id': 1}
        result_data = gate_client.charge_hold(initial_data)
        expected_data = initial_data
        expected_data['guid'] = 'AAAA-AAAA-AAAA-AAAA'
        expected_data['account_guid'] = 'AAAA-AAAA-AAAA-AAAA'
        expected_data['pwd'] = hashlib.sha1('111').hexdigest()
        req_class.executeRequest.assert_called_once_with('charge_hold', expected_data)

    @patch('lib.gateclient.Request')
    def test_cancel_dms_request(self, req_mock):
        req_class = Mock()
        req_class.executeRequest.return_value = None
        req_mock.return_value = req_class

        gate_client = GateClient('https://www.payment-api.com', 'AAAA-AAAA-AAAA-AAAA', '111')

        initial_data = {
            'init_transaction_id': '123123',
            'amount_to_refund': '1000'}
        result_data = gate_client.cancel_dms(initial_data)
        expected_data = initial_data
        expected_data['guid'] = 'AAAA-AAAA-AAAA-AAAA'
        expected_data['account_guid'] = 'AAAA-AAAA-AAAA-AAAA'
        expected_data['pwd'] = hashlib.sha1('111').hexdigest()
        req_class.executeRequest.assert_called_once_with('cancel_dms', expected_data)
        
    
    @patch('lib.gateclient.Request')
    def test_status_request(self, req_mock):
        req_class = Mock()
        req_class.executeRequest.return_value = None
        req_mock.return_value = req_class

        gate_client = GateClient('https://www.payment-api.com', 'AAAA-AAAA-AAAA-AAAA', '111')

        initial_data = {'init_transaction_id': '2250fcc6fd097e7b9df02aa9b95bf46baa7f8fea', 'f_extended': '5', 'request_type': 'transaction_status'}
        result_data = gate_client.status(initial_data)
        expected_data = initial_data
        expected_data['guid'] = 'AAAA-AAAA-AAAA-AAAA'
        expected_data['pwd'] = hashlib.sha1('111').hexdigest()
        expected_data['account_guid'] = 'AAAA-AAAA-AAAA-AAAA'
        req_class.executeRequest.assert_called_once_with('status', expected_data)
