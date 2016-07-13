from .signer import Signer
from .cipher import Cipher
from .payload import Payload
import json


class TokenManager:
    """
        Generate token from uid
        Verify token from request
    """
    __salt_size = 32

    def __payload_to_token(self, payload):
        """
        Generate token from payload instance
        :param payload:
        :return:
        """


    def to_token(self, uid, secret_key, token_ttl=300, remember_ttl=0):
        """
        Generate token by create payload and call __payload_to_token
        :param uid:
        :param secret_key:
        :param token_ttl
        :param remember_ttl
        :return:
        """
        salt = Cipher.generate_salt()
        payload = Payload.new(uid, secret_key, salt, token_ttl, remember_ttl)
