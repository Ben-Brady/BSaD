from flask import render_template, request, redirect
from modules import flask, users


def get_index():
    user = flask.parse_token(request)
    if user is None:
        return redirect("/login")
    if user.role == "admin":
        return redirect("/admin")
    else:
        return render_template(
            "index.html",
            user=user
        )


def get_admin():
    user = flask.parse_token(request)
    if user is None or user.role != "admin":
        return redirect("/")

    return render_template(
        "admin.html",
        user=user,
        accounts=list(users.list_users()),
    )

def get_application():
    user = flask.parse_token(request)
    if user is None:
        return redirect("/")

    return render_template(
        "application.html",
        user=user,
        accounts=list(users.list_users()),
    )

def get_testing():
    user = flask.parse_token(request)
    if user is None:
        return redirect("/")

    return render_template(
        "testing.html",
        user=user,
        accounts=list(users.list_users()),
    )
