from flask import request, redirect, render_template, redirect, Request
from modules import account


def get_login():
    error = request.args.get("error", "")
    return render_template(
        "login.html",
        error=error,
    )


def post_login():
    username = str(request.form.get("username"))
    password = str(request.form.get("password"))
    success = account.login(username, password)

    if success == False:
        return redirect("/login?error=Login%20Failed")
    else:
        user = account.get_account(username)
        token = account.create_token(user)

        resp = redirect("/")
        resp.set_cookie("token", token)
        return resp


def get_logout():
    resp = redirect("/")
    resp.delete_cookie("token")
    return resp


def parse_token(req: Request) -> account.Account|None:
    token = req.cookies.get("token")
    if token is None:
        return None

    try:
        user = account.decode_token(token)
    except Exception:
        return None

    return user
