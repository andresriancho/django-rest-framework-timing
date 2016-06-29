import time

from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions


class DelayTokenAuthentication(TokenAuthentication):
    """
    Simple token based authentication with configurable delay

    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string "Token ".  For example:

        Authorization: Token 401f7ac837da42b97f613d789819ff93537bee6a
    """
    HARDCODED_TOKEN = '224a93060c0dd4fb931d05083b4cb7b6a8c27df8'
    DELAY = 0.001

    def authenticate_credentials(self, key):
        if len(key) != len(self.HARDCODED_TOKEN):
            raise exceptions.AuthenticationFailed('Invalid token.')

        for i in xrange(len(key)):
            if key[i] == self.HARDCODED_TOKEN[i]:
                time.sleep(self.DELAY)
            else:
                raise exceptions.AuthenticationFailed('Invalid token.')
