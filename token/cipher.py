import base64

from Crypto.Cipher import AES
from Crypto import Random
from hashlib import md5


class Cipher:
    """
        Encrypt/Decrypt string by AES SSl
    """
    __block_size_ = AES.block_size
    __AES_MODE_ = AES.MODE_CFB
    key_length = 32

    @classmethod
    def generate_salt(self, size=32):
        """
        Generate random salt
        :param size:
        :return:
        """
        return base64.b64encode(Random.new().read(size)).decode()

    @classmethod
    def to_iv(self, password, salt):
        """
        Hash iv, key from password, salt
        md5 recursive
        :param password:
        :param salt:
        :return:
        """
        d = d_i = b""
        password = password.encode("utf-8")
        salt = salt.encode("utf-8")
        while len(d) < self.__block_size_ + self.key_length:
            d_i = md5(password + salt + d_i).digest()
            d += d_i
        return d[:self.key_length], d[self.key_length:self.key_length + self.__block_size_]

    @classmethod
    def encrypt(self, data, password, salt):
        """
        Encrypt data to byte, and convert to base64

        :param data:
        :param password:
        :param salt:
        :return:
        """
        key, iv = self.to_iv(password, salt)
        cipher = AES.new(key, self.__AES_MODE_, iv)

        return base64.b64encode(cipher.encrypt(data)).decode()

    @classmethod
    def decrypt(self, data, password, salt):
        """
        Decrypt string base64 data
        :param data:
        :param password:
        :param salt:
        :return:
        """
        try:
            data = base64.b64decode(data)
            key, iv = self.to_iv(password, salt)
            cipher = AES.new(key, self.__AES_MODE_, iv)
            return cipher.decrypt(data).decode()
        except:
            return None
