import hashlib

from lib.request import Request
from lib.validator import Validator

class GateClient:

    def __init__(self, apiUrl, guid, pwd, verifySSL=True):
        pwd_shal = hashlib.sha1(pwd)
        self.access_data = {'apiUrl': apiUrl, 'guid': guid, 'pwd': pwd_shal.hexdigest(), 'verifySSL': verifySSL}

    def __build_data(self, data):
        data['guid'] = self.access_data['guid']
        data['pwd'] = self.access_data['pwd']
        return data

    def init(self, data):
        validator = Validator('init', data)
        request_data = self.__build_data(validator.execute())
        req = Request(self.access_data['apiUrl'], self.access_data['verifySSL'])
        return req.executeRequest('init', request_data)

    def charge(self, data):
        validator = Validator('charge', data)
        request_data = self.__build_data(validator.execute())
        req = Request(self.access_data['apiUrl'], self.access_data['verifySSL'])
        return req.executeRequest('charge', request_data)