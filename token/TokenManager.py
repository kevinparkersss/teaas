import json

from . import signer, cipher, payload

class TokenManager:
    """
        Generate token
    """

    def to_token(self, uid, secret_key, ):
