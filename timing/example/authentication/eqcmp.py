from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions


class EqCmpTokenAuthentication(TokenAuthentication):
    """
    Simple token based authentication using a HARD CODED token

    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string "Token ".  For example:

        Authorization: Token 401f7ac837da42b97f613d789819ff93537bee6a
    """
    HARDCODED_TOKEN = '224a93060c0dd4fb931d05083b4cb7b6a8c27df8'

    def authenticate_credentials(self, key):
        if key != self.HARDCODED_TOKEN:
            raise exceptions.AuthenticationFailed('Invalid token.')
