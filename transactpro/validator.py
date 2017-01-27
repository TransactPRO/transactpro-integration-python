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
            'init_dms': self.validate_data_init,
            'make_hold': self.validate_data_charge,
            'charge_hold': self.validate_charge_hold,
            'cancel_dms': self.validate_data_refund,
            'status': self.validate_data_status,
            'init_credit': self.validate_data_init_credit,
            'do_credit': self.validate_data_do_credit,
            'init_p2p': self.validate_data_init_p2p,
            'do_p2p': self.validate_data_do_p2p,
            'init_recurrent_credit': self.validate_charge_recurrent,
            'do_recurrent_credit': self.validate_charge_recurrent,
            'init_recurrent_p2p': self.validate_charge_recurrent,
            'do_recurrent_p2p': self.validate_charge_recurrent
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
            if self.data.get(option_name) is not None or default_value != '':
                initial_data[option_name] = self.data.get(option_name, default_value)
        return initial_data

    # Here comes all validate methods

    def validate_data_init(self):
        mandatory_field_list = ['rs', 'merchant_transaction_id', 'user_ip', 'description', 'amount', 'currency',
                                'name_on_card', 'street', 'zip', 'city', 'country', 'email', 'phone',
                                'merchant_site_url']
        optional_fields_dict = {'state': 'NA', 'card_bin': 'NA', 'bin_name': 'NA', 'bin_phone': '',
                                'save_card': '', 'shipping_phone': '', 'shipping_email': '', 'shipping_state': '',
                                'shipping_country': '', 'shipping_city': '', 'shipping_zip': '', 'shipping_street': ''}
        return self.__validate_process(mandatory_field_list, optional_fields_dict)

    def validate_data_charge(self):
        mandatory_field_list = ['init_transaction_id', 'cc', 'cvv', 'expire']
        optional_fields_dict = {'f_extended': '', 'merchant_referring_url': ''}
        return self.__validate_process(mandatory_field_list, optional_fields_dict)

    def validate_data_refund(self):
        mandatory_field_list = ['init_transaction_id', 'amount_to_refund']
        optional_fields_dict = {'merchant_transaction_id': '', 'details': ''}
        return self.__validate_process(mandatory_field_list, optional_fields_dict)

    def validate_init_recurrent(self):
        mandatory_field_list = ['rs', 'original_init_id', 'merchant_transaction_id', 'amount', 'description']
        return self.__validate_process(mandatory_field_list)

    def validate_charge_recurrent(self):
        mandatory_field_list = ['init_transaction_id']
        optional_fields_dict = {'f_extended': ''}
        return self.__validate_process(mandatory_field_list, optional_fields_dict)

    def validate_charge_hold(self):
        mandatory_field_list = ['init_transaction_id']
        return self.__validate_process(mandatory_field_list)

    def validate_data_status(self):
        mandatory_field_list = ['init_transaction_id']
        optional_fields_dict = {'f_extended': '5', 'request_type': 'transaction_status'}
        return self.__validate_process(mandatory_field_list, optional_fields_dict)

    def validate_data_init_credit(self):
        mandatory_field_list = ['rs', 'merchant_transaction_id', 'user_ip', 'description', 'amount', 'currency',
                                'name_on_card', 'street', 'zip', 'city', 'country', 'email', 'phone',
                                'merchant_site_url']
        optional_fields_dict = {'state': 'NA', 'card_bin': 'NA', 'bin_name': 'NA', 'bin_phone': '',
                                'save_card': '', 'shipping_phone': '', 'shipping_email': '', 'shipping_state': '',
                                'shipping_country': '', 'shipping_city': '', 'shipping_zip': '', 'shipping_street': ''}
        return self.__validate_process(mandatory_field_list, optional_fields_dict)

    def validate_data_do_credit(self):
        mandatory_field_list = ['init_transaction_id', 'cc']
        optional_fields_dict = {'f_extended': '', 'expire': ''}
        return self.__validate_process(mandatory_field_list, optional_fields_dict)

    def validate_data_init_p2p(self):
        mandatory_field_list = ['cardname', 'recipient_name', 'client_birth_date', 'rs', 'merchant_transaction_id',
                                'user_ip', 'description', 'amount', 'currency', 'name_on_card', 'street', 'zip',
                                'city', 'country', 'email', 'phone', 'merchant_site_url']
        optional_fields_dict = {'state': 'NA', 'card_bin': 'NA', 'bin_name': 'NA', 'bin_phone': '',
                                'save_card': '', 'shipping_phone': '', 'shipping_email': '', 'shipping_state': '',
                                'shipping_country': '', 'shipping_city': '', 'shipping_zip': '', 'shipping_street': ''}
        return self.__validate_process(mandatory_field_list, optional_fields_dict)

    def validate_data_do_p2p(self):
        mandatory_field_list = ['init_transaction_id', 'cc_2']
        optional_fields_dict = {'f_extended': '', 'expire2': ''}
        return self.__validate_process(mandatory_field_list, optional_fields_dict)
