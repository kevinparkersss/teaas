class Payload:
    """
        Payload store token information
        :__token_ttl_ -> lifetime of token
        :__remember_ttl_ -> lifetime of remember key
        :__uid_ -> account id
        :__secret_key_ -> Secret Key
    """

    __token_ttl_ = 300  #: second
    __remember_ttl_ = 0  #: second
    __secret_key_ = ""
    __uid_ = None

    def __init__(self, uid=None, secret_key=None, token_ttl=300, remember_ttl=0):
        self.__token_ttl_ = token_ttl
        self.__remember_ttl_ = remember_ttl
        self.__secret_key_ = secret_key
        self.__uid_ = uid

    def to_json(self):
        """
        
        :return:
        """

    @classmethod
    def new(cls, uid=None, secret_key=None, token_ttl=300, remember_ttl=0):
        return Payload(uid, secret_key, token_ttl, remember_ttl)
