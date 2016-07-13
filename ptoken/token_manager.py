from .cipher import Cipher
from .payload import Payload
from hashlib import md5


class TokenManager:
    """
        Generate token from uid
        Verify token from request
    """

    @classmethod
    def to_token(cls, uid, secret_key, token_ttl=10, remember_ttl=86500):
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

    @classmethod
    def from_token(cls, token, secret_key):
        """
        Decrypt token and verify token
        :param token:
        :return:
        """

        salt = md5(secret_key.encode("utf-8")).hexdigest()
        token = Cipher.decrypt(token, secret_key, salt)
        if token is None:
            return False

        pl = Payload(secret_key=secret_key, salt=salt)
        if not pl.load(token):
            return False

        return pl.verify()
