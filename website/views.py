#here we are storing all routes of website. ((Login page not, because it has to do with authentication), Home page, etc.)

from flask import Blueprint, render_template, request, jsonify, redirect, url_for
 #Blueprint has many roots / URLs inside it

views = Blueprint("views", __name__)

@views.route("/")
#this function will run, whenever we go to the /-route: ""
def home():
    return '<h1>Test</h1>'


