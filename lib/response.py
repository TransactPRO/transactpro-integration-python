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

    def is_success(self):
        return self.status == SUCCESS

    def get_status(self):
        return self.status

    def get_content(self):
        return self.content

    def get_formated_content(self):
        self.content.split(':', 1)
        return self.content
