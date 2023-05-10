from .auth import get_login, post_login, get_logout, parse_token
from .api import post_update_role, post_delete_user
from .templates import get_index, get_account, get_admin
from flask import Flask


def inject_routes(app: Flask):
    app.get("/")(get_index)
    app.get("/account")(get_account)
    app.get("/admin")(get_admin)

    app.get("/login")(get_login)
    app.post("/login")(post_login)
    app.get("/logout")(get_logout)

    app.post("/api/update-role")(post_update_role)
    app.post("/api/delete-user")(post_delete_user)
