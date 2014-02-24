__author__ = 'olga'

from lib.validator import Validator

class GateClient:

    def __init__(self, apiUrl, guid, pwd, verifySSL=True):
        self.access_data = {'apiUrl': apiUrl, 'guid': guid, 'pwd': pwd, 'verifySSL': verifySSL}

    def __build_data(self, data):
        data['guid'] = self.access_data['guid']
        data['pwd'] = self.access_data['pwd']
        return data

    def init(self, data):
        validator = Validator('init', data)
        request_data = self.__build_data(validator.execute())