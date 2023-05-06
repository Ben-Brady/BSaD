from .login import get_login, post_login, get_logout
from flask import Flask


def inject_routes(app: Flask):
    app.get("/login")(get_login)
    app.post("/login")(post_login)
    app.get("/logout")(get_logout)
