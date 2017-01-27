from unittest import TestCase
from transactpro.validator import Validator
from transactpro.errors import MissingFieldException


class TestValidator(TestCase):
    def test_validate_charge_success(self):
        data = {'init_transaction_id': 1, 'cc': '1234123412341234', 'cvv': '987', 'expire': '12/15'}
        validator = Validator('charge', data)
        expected = dict(data.items())
        self.assertEquals(validator.execute(), expected)

    def test_validate_charge_raise_mandatory_error(self):
        data = {'init_transaction_id': 1, 'cc': '1234123412341234', 'expire': '12/13'}
        validator = Validator('charge', data)
        self.assertRaises(MissingFieldException, validator.execute)

    def test_validate_charge_option_arg_supplied(self):
        data = {'init_transaction_id': 1, 'cc': '1234123412341234', 'cvv': '666', 'expire': '12/13', 'f_extended': 3}
        validator = Validator('charge', data)
        self.assertEquals(validator.execute(), data)

    def test_validate_data_init_state(self):
        data = {
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
        validator = Validator('init', data)
        self.assertEquals(validator.execute(), data)

    def test_validate_data_init_no_state(self):
        data = {
            'rs': '1111',
            'merchant_transaction_id': '12390',
            'user_ip': '127.0.0.1',
            'description': 'My description',
            'amount': '1000',
            'currency': 'USD',
            'name_on_card': 'Vasyly Pupkin',
            'street': 'Main street 1',
            'zip': 'LV-0000',
            'city': 'Riga',
            'country': 'LV',
            'email': 'email@example.lv',
            'phone': '111',
            'card_bin': '511111',
            'bin_name': 'BANK',
            'bin_phone': '+371 11111111',
            'merchant_site_url': 'https://example.com'}
        validator = Validator('init', data)
        expected = dict(data.items() + {'state': 'NA'}.items())
        self.assertEquals(validator.execute(), expected)

    def test_validate_data_refund(self):
        data = {'init_transaction_id': '1212321323213213', 'amount_to_refund': '40'}
        validator = Validator('refund', data)
        self.assertEquals(validator.execute(), data)

    def test_validate_init_recurrent(self):
        data = {
            'rs': '1223',
            'original_init_id': 2,
            'merchant_transaction_id': 1,
            'amount': '1000',
            'description': 'Recurrent money'}
        validator = Validator('init_recurrent', data)
        self.assertEquals(validator.execute(), data)

    def test_validate_data_charge_recurrent(self):
        data = {
            'init_transaction_id': '2250fcc6fd097e7b9df02aa9b95bf46baa7f8fea'}
        validator = Validator('charge_recurrent', data)
        self.assertEquals(validator.execute(), data)

    def test_validate_data_init_dms(self):
        data = {
            'rs': '888',
            'merchant_transaction_id': '121212121212',
            'user_ip': '127.0.0.1',
            'description': 'DMS transaction',
            'amount': '1000',
            'currency': 'USD',
            'name_on_card': 'Vasyly Pupkin',
            'street': 'Main street 1',
            'zip': '41212213',
            'city': 'Riga',
            'state': 'MyState',
            'country': 'LV',
            'email': 'email@example.lv',
            'phone': '+371 11111111',
            'card_bin': '511111',
            'bin_name': 'BANK',
            'bin_phone': '+371 11111111',
            'merchant_site_url': 'https://test.com'}
        validator = Validator('init_dms', data)
        self.assertEquals(validator.execute(), data)

    def test_validate_charge_hold(self):
        data = {'init_transaction_id': 1}
        validator = Validator('charge_hold', data)
        self.assertEquals(validator.execute(), data)

    def test_validate_cancel_dms(self):
        data = {'init_transaction_id': '1212321323213213', 'amount_to_refund': '40'}
        validator = Validator('cancel_dms', data)
        self.assertEquals(validator.execute(), data)

    def test_validate_status(self):
        data = {'init_transaction_id': '1212321323213213'}
        validator = Validator('status', data)
        data['request_type'] = 'transaction_status'
        data['f_extended'] = '5'
        self.assertEquals(validator.execute(), data)

    def test_validate_init_credit(self):
        data = {
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
        validator = Validator('init_credit', data)
        self.assertEquals(validator.execute(), data)

    def test_validate_do_credit(self):
        data = {'init_transaction_id': 'aASDLKJL1237123717313798asda',
                'cc': '1234123412341234',
                'expire': '12/20'}
        validator = Validator('do_credit', data)
        self.assertEquals(validator.execute(), data)

    def test_validate_init_p2p(self):
        data = {
            'cardname': 'BAT CAT',
            'recipient_name': 'CAT WOMAN',
            'client_birth_date': '06161981',
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
        validator = Validator('init_p2p', data)
        self.assertEquals(validator.execute(), data)

    def test_validate_do_p2p(self):
        data = {'init_transaction_id': 'aASDLKJL1237123717313798asda',
                'cc_2': '1234123412341234',
                'expire2': '10/30'}
        validator = Validator('do_p2p', data)
        self.assertEquals(validator.execute(), data)

    def test_validate_init_recurrent_credit(self):
        data = {
            'rs': '1223',
            'original_init_id': 2,
            'merchant_transaction_id': 1,
            'amount': '1000',
            'description': 'Recurrent money'}
        validator = Validator('init_recurrent_credit', data)
        self.assertEquals(validator.execute(), data)

    def test_validate_do_recurrent_credit(self):
        data = {
            'init_transaction_id': '2250fcc6fd097e7b9df02aa9b95bf46baa7f8fea'}
        validator = Validator('do_recurrent_credit', data)
        self.assertEquals(validator.execute(), data)

    def test_validate_init_recurrent_p2p(self):
        data = {
            'rs': '1223',
            'original_init_id': 2,
            'merchant_transaction_id': 1,
            'amount': '1000',
            'description': 'Recurrent money'}
        validator = Validator('init_recurrent_p2p', data)
        self.assertEquals(validator.execute(), data)

    def test_validate_do_recurrent_p2p(self):
        data = {
            'init_transaction_id': '2250fcc6fd097e7b9df02aa9b95bf46baa7f8fea'}
        validator = Validator('do_recurrent_p2p', data)
        self.assertEquals(validator.execute(), data)
