from typing import Literal, Union
from dataclasses import dataclass
import jwt

SECRET = "SECRET_PASSWORD"

@dataclass
class Account:
    username: str
    display_name: str
    password: str
    role: Literal["application", "operate", "resiliency", "admin"]


accounts = {
    "admin": Account("admin", "Administrator", "password", "admin"),
    "bob": Account("bob", "Bob Bobertson", "password", "application"),
    "carl": Account("carl", "Carl Carlson", "password", "operate"),
    "daniel": Account("daniel", "Daniel Davidson", "password", "resiliency"),
}


def login(username: str, password: str) -> bool:
    account = accounts.get(username, None)
    if account is None:
        return False
    if account.password != password:
        return False
    return True


def get_account(username: str) -> Account:
    return accounts[username]


def create_token(account: Account) -> str:
    return jwt.encode({
        "username": account.username
    }, SECRET, algorithm="HS256")


def decode_token(token: str) -> Account:
    data = jwt.decode(token, SECRET, algorithms=["HS256"])
    username = data["username"]
    return get_account(username)

