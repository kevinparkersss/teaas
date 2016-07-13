from ptoken import token_manager

from ptoken.cache.backend.redis import Redis

Redis.create_pool("127.0.0.1", None, 1)

Redis.set("tests", "1111113", ttl=1)

print(Redis.get("tests"))