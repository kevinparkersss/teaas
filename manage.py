import sys, importlib
from ptoken.cache.frontend import Frontend as Cache

t = Cache("Redis", host="127.0.0.1")
t.set("test", "value", ttl="1")
t.remove("dasd", "test")
print(t.get("test"))
print(t.has("test"))

#
# Redis.__create_pool("127.0.0.1", None, 1)
#
# # Redis.set("tests", "1111113", ttl=1)
#
# print(Redis.has("tests"))
