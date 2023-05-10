from . import User, get_user
import jwt

SECRET = "SECRET_PASSWORD"


def create_auth_token(account: User) -> str:
    return jwt.encode({
        "id": account.id
    }, SECRET, algorithm="HS256")


def decode_auth_token(token: str) -> User|None:
    data = jwt.decode(token, SECRET, algorithms=["HS256"])
    user_id = data["id"]
    return get_user(user_id)
