from ptoken.token_manager import TokenManager
from ptoken.cache.frontend import Frontend as CacheMgr
from ptoken.cache.backend import Redis as Redis
import time

if __name__ == "__main__":
    cache_mgr = CacheMgr("Redis", host="127.0.0.1", port=6379, db=2)

    token_mgr = TokenManager.getInstance(
        secret_key="token-Na5xKNsU/Tw/W93X4q+hDtQiY8eCof2R1pUZg2BW/jb19mcpJpxrfHjH78vO1NjcjH+Ovv/H5aPe3kBaBh1BqwqyrAWAvxe+vI10Bcd7LW7rf36ychBuJhbmMS3qrRIDgZ0B6cI7fzJ2SPf5iO1SOIu55G+SqA+7ybgoHyiB7kzSYczxsOwgj3tXV0810lj2XnUkGeKwU0iLWdNDzFwEm+TNCHeB4c/iatxe2DtlHVXRryidKJPNBBbr5tCCZw279TPAHWWCs5rE4nvnnnYhcbNAjctoZzXPEJ0xXia4jybQ5iT/xHcAqupPiUarZCv+DAP4xRw62+rY+jmslPoZP2oOOP6anamkBrLvna/Jzd56WxpLw+GRhmoViJTGIKD3kHe7SAvovdFKfDJOLVPOc3/lx44MtYQHvcekLS3g/1lCVe0mCxMqIo/3JY2jzveCrS2NwwwuC8Zv4mMPpMajpXhfZOEYOgZbZeGi91X+l5pzWw==",
        cache=cache_mgr,
        token_ttl=5
    )
    token, remember_key = token_mgr.to_token(1)
    time.sleep(6)
    print(token_mgr.from_token(token, remember_key))
