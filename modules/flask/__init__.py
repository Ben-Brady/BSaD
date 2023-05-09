from .auth import get_login, post_login, get_logout, parse_token
from .templates import get_index, get_account
from flask import Flask


def inject_routes(app: Flask):
    app.get("/")(get_index)
    app.get("/account")(get_account)
    app.get("/login")(get_login)
    app.post("/login")(post_login)
    app.get("/logout")(get_logout)
