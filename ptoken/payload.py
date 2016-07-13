import json, redis

from .signer import Signer
from .cipher import Cipher


class Payload:
    """
        Payload store token information
        :__token_ttl_: lifetime of token
        :__remember_ttl_: lifetime of remember key
        :__uid_: account id
        :__secret_key_: Secret Key
        :____signature_: Signature is be generated
        :__salt_: salt for encrypt
    """

    __token_ttl_ = 300  #: second
    __remember_ttl_ = 0  #: second
    __salt_ = ""
    __signature_ = ""
    __secret_key_ = ""
    __uid_ = None

    def __init__(self, uid=None, secret_key="", salt="", token_ttl=300, remember_ttl=0):
        self.__token_ttl_ = token_ttl
        self.__remember_ttl_ = remember_ttl
        self.__secret_key_ = secret_key
        self.__uid_ = uid
        self.__salt_ = salt

    @classmethod
    def new(cls, uid=None, secret_key="", salt="", token_ttl=300, remember_ttl=0):
        return Payload(uid, secret_key, salt, token_ttl, remember_ttl)

    @property
    def token_ttl(self):
        return self.__token_ttl_

    @property
    def remember_ttl(self):
        return self.__remember_ttl_

    @property
    def salt(self):
        return self.__salt_

    @property
    def secret_key(self):
        return self.__secret_key_

    @property
    def uid(self):
        return self.__uid_

    def sign(self):
        """"""