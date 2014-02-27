from unittest import TestCase
from lib.validator import Validator
from lib.errors import MissingFieldException


class TestValidator(TestCase):
    def test_validate_charge_success(self):
        data = {'init_transaction_id': 1, 'cc': '1234123412341234', 'cvv': '987', 'expire': '12/15'}
        validator = Validator('charge', data)
        expected = dict(data.items() + {'f_extended': ''}.items())
        self.assertEquals(validator.execute(), expected)

    def test_validate_charge_raise_mandatory_error(self):
        data = {'init_transaction_id': 1, 'cc': '1234123412341234', 'expire': '12/15'}
        validator = Validator('charge', data)
        self.assertRaises(MissingFieldException, validator.execute)

    def test_validate_charge_option_arg_supplied(self):
        data = {'init_transaction_id': 1, 'cc': '1234123412341234', 'cvv': '987', 'expire': '12/15', 'f_extended': 3}
        validator = Validator('charge', data)
        self.assertEquals(validator.execute(), data)