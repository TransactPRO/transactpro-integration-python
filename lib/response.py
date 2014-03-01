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

    def get_formatted_content(self):
        if self.status == FAILURE:
            return {}

        parsed_response = {}
        key_value_pairs = self.content.split('~')

        for pair in key_value_pairs:
            try:
                (key, value) = pair.split(':', 1)
            except ValueError:      # This is case, when it errors to split "string:" into two strings
                key = pair.split(':', 1)
                value = ''
            parsed_response[key] = value
            
        return parsed_response