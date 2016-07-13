import redis
from .backend import Backend


class Redis(Backend):
    """
    Redis cache backend
    :pool: Redis connection
    """

    pool = None  # type:redis.ConnectionPool

    @classmethod
    def create_pool(cls, host="127.0.0.1", password=None, db=0, port=6379, max_connections=10, force=False):
        if cls.pool != None and force == False:
            cls.pool.disconnect()
            return
        cls.pool = redis.ConnectionPool(host=host, port=port, db=db, max_connections=max_connections)

    @classmethod
    def get(cls, key, default=None, **kwargs):
        """

        :param key:
        :param default:
        :param kwargs:
        :return:
        """
        connection = redis.Redis(connection_pool=cls.pool)
        result = connection.get(key)
        return result.decode() if not result == None else default

    @classmethod
    def set(cls, key, value, **kwargs):
        """
        Keyword Args:
            ttl (int): lifetime of key
        :param kwargs:
        :return:
        """

        connection = redis.Redis(connection_pool=cls.pool)
        if kwargs.get("ttl", None) == None:
            return connection.set(key, value)
        else:
            return connection.setex(key, value, int(kwargs.get("ttl")))
