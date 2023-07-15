#here we are storing all the stuff for the authentication of users. Login page, etc.

from flask import Blueprint, render_template #, request, jsonify, redirect, url_for
 #Blueprint has many roots / URLs inside it

auth = Blueprint("auth", __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>logout<p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")