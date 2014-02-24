""" Response logic
"""

SUCCESS = True
FAILURE = False

class Response(object):
    def __init__(self, status, content):
        if status == SUCCESS:
            self.status = SUCCESS
        else:
            self.status = FAILURE
        self.content = content

    def isSuccess(self):
        return self.status == SUCCESS

    def getStatus(self):
        return self.status

    def getContent(self):
        return self.content
