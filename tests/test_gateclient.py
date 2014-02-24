__author__ = 'olga'

from unittest import TestCase
from lib.gateclient import GateClient

class testGateClient(TestCase):

    def test_GateClient(self):
        gate_client = GateClient('123',"1234")
        assert (gate_client.accessData, '123')
