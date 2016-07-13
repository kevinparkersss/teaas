from .signer import Signer
from .cipher import Cipher
from .payload import Payload
from hashlib import md5
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

    @classmethod
    def to_token(cls, uid, secret_key, token_ttl=300, remember_ttl=0):
        """
        Generate token by create payload and call __payload_to_token
        :param uid:
        :param secret_key:
        :type secret_key str
        :param token_ttl
        :param remember_ttl
        :return:
        """

        salt = md5(secret_key.encode("utf-8")).hexdigest()
        pl = Payload.new(uid=uid, secret_key=secret_key, salt=salt, token_ttl=token_ttl, remember_ttl=remember_ttl)
        token = Cipher.encrypt(pl.sign()[1].encode(), secret_key, salt)
        return token
