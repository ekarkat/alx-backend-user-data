#!/usr/bin/env python3
"""FLASK APP module"""

from flask import Flask, jsonify, request, abort, jsonify, make_response
from flask import redirect
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """Simple Route"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """Register user route"""
    email = request.form.get('email')
    pwd = request.form.get('password')
    try:
        AUTH.register_user(email, pwd)
        return jsonify({"email": email, "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """Session login route"""
    email = request.form.get('email')
    pwd = request.form.get('password')
    if AUTH.valid_login(email, pwd):
        response = make_response(jsonify({"email": email,
                                          "message": "logged in"}))
        response.set_cookie('session_id', AUTH.create_session(email))
        return response
    else:
        abort(401)


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout() -> str:
    """Logout route"""
    user_cookie = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(user_cookie)
    if user:
        AUTH.destroy_session(user.id)
        return redirect("/")
    abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token_route() -> str:
    """reset pwd route"""
    email = request.form.get('email')
    if AUTH.create_session(email):
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": token})
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
