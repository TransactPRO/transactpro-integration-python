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
        if self.get_status() == FAILURE:
            return []

        parsedResponse = {}
        key_value_pairs = self.content.split('~')
        print key_value_pairs
        for keyValuePair in key_value_pairs:
            keyValue = keyValuePair.split(':', 1)
            if keyValue[1] is not None:
                parsedResponse[keyValue[0]] = keyValue[1]
            else:
                parsedResponse[keyValue[0]] = ''
        return parsedResponse