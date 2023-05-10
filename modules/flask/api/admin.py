from flask import request, redirect, render_template, redirect, Request
from modules import users


def post_update_role():
    user_id = request.form.get("id", "")
    role = request.form.get("role")
    if role is None or role not in users.valid_roles:
        return "Invalid role", 400

    if not users.user_exists(user_id):
        return "User does not exist", 400

    users.change_role(user_id, role)
    return "", 200


def post_delete_user():
    user_id = request.form.get("id", "")
    if user_id is None or not users.user_exists(user_id):
        return "User Does Not Exist", 400

    users.delete_user(user_id)
    return "", 200
