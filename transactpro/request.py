""" Request logic
"""
import pycurl
import response
import urllib
import StringIO


class Request(object):
    def __init__(self, url, verifySSL=True):
        self.url = url + '/gwprocessor2.php?a='
        self.verifySSL = verifySSL

    def executeRequest(self, action, post_data):
        curl = pycurl.Curl()  # main handler for Curl actions

        # Setting request params
        self.action_url = self.url + action
        curl.setopt(pycurl.URL, self.action_url)
        curl.setopt(pycurl.FAILONERROR, True)
        curl.setopt(pycurl.FOLLOWLOCATION, 1)
        curl.setopt(pycurl.TIMEOUT, 30)
        curl.setopt(pycurl.POST, True)
        if self.verifySSL:
            curl.setopt(pycurl.SSL_VERIFYHOST, 2)
            curl.setopt(pycurl.SSL_VERIFYPEER, 1)
        curl.setopt(pycurl.POSTFIELDS, urllib.urlencode(post_data))

        # Required for reading output
        buffer = StringIO.StringIO()

        curl.setopt(pycurl.WRITEFUNCTION, buffer.write)

        curl.perform()  # Execute request

        content = buffer.getvalue()
        if content == "":
            status = response.FAILURE
            content = curl.errstr()
        else:
            status = response.SUCCESS

        buffer.close()
        curl.close()
        return response.Response(status, content)
