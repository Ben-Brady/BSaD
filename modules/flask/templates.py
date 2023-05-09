from modules import account, flask
from flask import render_template, request, redirect

def get_index():
    user = flask.parse_token(request)
    if user == None:
        return redirect("/login")
    else:
        return render_template("index.html", user=user)


def get_account():
    user = flask.parse_token(request)
    if user == None:
        return redirect("/")

    return render_template(
        "account.html",
        user=user,
        accounts=list(account.accounts.values()),
    )
