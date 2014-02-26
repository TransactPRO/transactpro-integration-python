import errors
import os
import cgi

class Validator(object):

    def __init__(self, action, data):
        self.action = action
        self.data = data
        self.validate_method = {
            'init': self.validate_data_init,
            'charge': self.validate_data_charge,
            'refund': self.validate_data_refund,
            'init_recurrent': self.validate_init_recurrent,
            'charge_recurrent': self.validate_charge_recurrent,
        }

    def execute(self):
        return self.validate_method[self.action]()

    def __validate_process(self, mandatory_field_list, optional_fields_dict={}):
        data = self.__check_mandatory_args(mandatory_field_list)
        data = self.__check_optional_args(data, optional_fields_dict)
        return data

    def __check_mandatory_args(self, name_list):
        data = {}
        try:
            # Check mandatory fields
            for each in name_list:
                data[each] = self.data[each]
        except KeyError, e:
            raise errors.MissingFieldException(e)

        return data

    def __check_optional_args(self, initial_data, options_dict):
        for option_name, default_value in options_dict.iteritems():
            initial_data[option_name] = self.data.get(option_name, default_value)

        return initial_data

    # Here comes all validate methods

    def validate_data_init(self):
        mandatory_field_list = ['rs', 'merchant_transaction_id', 'description', 'amount', 'currency', 'name_on_card',
                                'street', 'zip', 'city', 'country', 'phone', 'merchant_site_url']
        optional_fields_dict = {'user_ip': '127.0.0.1', 'state': 'NA', 'email': '',
                                'card_bin': '', 'bin_name': '', 'bin_phone': '', 'save_card': ''}
        return self.__validate_process(mandatory_field_list, optional_fields_dict)

    def validate_data_charge(self):
        mandatory_field_list = ['init_transaction_id', 'cc', 'cvv', 'expire']
        optional_fields_dict = { 'f_extended': '' }
        return self.__validate_process(mandatory_field_list, optional_fields_dict)

    def validate_data_refund(self):
        mandatory_field_list = ['init_transaction_id', 'amount_to_refund']
        return self.__validate_process(mandatory_field_list)

    def validate_init_recurrent(self):
        mandatory_field_list = ['rs', 'original_init_id', 'merchant_transaction_id', 'amount']
        optional_fields_dict = {'description':''}
        return self.__validate_process(mandatory_field_list, optional_fields_dict)

    def validate_charge_recurrent(self):
        mandatory_field_list = ['init_transaction_id']
        optional_fields_dict = {'f_extended': ''}
        return self.__validate_process(mandatory_field_list, optional_fields_dict)
