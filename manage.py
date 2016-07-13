from ptoken.token_manager import TokenManager
import time

if __name__ == "__main__":
    token = TokenManager.to_token(1, "123456")
    time.sleep(10)
    print(TokenManager.from_token(token, "123456"))
