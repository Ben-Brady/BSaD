from flask import request, make_response, render_template


accounts = {
    ("username", "password"): ("username", "role")
}

def get_login():
    return render_template("login.html")


def post_login():
    data = request.get_json()
    if data is None:
        return "no data sent", 400

    username = data.get("username", "none")
    password = data.get("password", "none")
    if (username, password) not in accounts:
        return "invalid username or password", 401
    else:
        resp = make_response("ok", 200)
        resp.set_cookie("username", "")
        resp.set_cookie("role", "")
        return resp


def get_logout():
    resp = make_response("ok", 200)
    resp.set_cookie("username", "")
    resp.set_cookie("role", "")
    return "", 200
