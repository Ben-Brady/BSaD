from flask import request, redirect, render_template, redirect, Request
from modules import users


def get_login():
    error = request.args.get("error", "")
    return render_template(
        "login.html",
        error=error,
    )


def post_login():
    user_id = str(request.form.get("username"))
    password = str(request.form.get("password"))
    success = users.login(user_id, password)

    if success == False:
        return redirect(f"{request.path}?error=Login%20Failed")

    user = users.get_user(user_id)
    token = users.create_auth_token(user)

    resp = redirect("/")
    resp.set_cookie("token", token)
    return resp


def get_logout():
    resp = redirect("/")
    resp.delete_cookie("token")
    return resp


def parse_token(req: Request) -> users.User | None:
    token = req.cookies.get("token")
    if token is None:
        return None

    try:
        user = users.decode_auth_token(token)
    except Exception:
        return None

    return user
