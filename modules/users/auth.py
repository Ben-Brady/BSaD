from . import get_user, user_exists

def login(username: str, password: str) -> bool:
    if not user_exists(username):
        return False

    account = get_user(username)
    if account.password != password:
        return False

    return True
