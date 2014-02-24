__author__ = 'olga'


class GateClient:

   def __init__(self, accessData, requestExecuter):
       self.access_data = accessData
       self.request_executor = requestExecuter