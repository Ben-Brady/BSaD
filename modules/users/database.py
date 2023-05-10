from . import User, Role

users: dict[str, User] = {}


def list_users() -> list[User]:
    return list(users.values())


def create_user(user: User):
    users[user.id] = user


def delete_user(id: str):
    users.pop(id)


def user_exists(id: str) -> bool:
    return id in users


def get_user(id: str) -> User|None:
    return users.get(id, None)


def change_role(id: str, role: str):
    """Raises:
        KeyError: User does not exist
    """
    if not user_exists(id):
        raise KeyError(f"User {id} does not exist")

    if role not in (
        "application",
        "operations",
        "resiliency",
        "admin",
        ):
        raise ValueError(f"Invalid role {role}")

    users[id].role = role


create_user(User(
    id="admin",
    name="Administrator",
    password="password",
    role="admin"
))
create_user(User(
    id="123",
    name="Bob Bobertson",
    password="password",
    role="application",
))
create_user(User(
    id="456",
    name="Carl Carlson",
    password="password",
    role="operations",
))
create_user(User(
    id="789",
    name="Daniel Davidson",
    password="password",
    role="resiliency",
))
