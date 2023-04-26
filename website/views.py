from flask import Blueprint, render_template, request, jsonify, redirect, url_for
 #Blueprint has many roots / URLs inside it

views = Blueprint(__name__, "views")



@views.route("/")
#this function will run, whenever we go to the /-route: "http://127.0.0.1:5000/"
def home():
    return '<h1>Test</h1>'


@views.route("/profile/")
def profile():
    args = request.args
    name = args.get("name")
    return render_template("index.html", name=name)

@views.route("/json")
def get_json():
    return jsonify({"name": "tim", "coolness": 10})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))