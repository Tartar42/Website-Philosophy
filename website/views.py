from flask import Blueprint, render_template, request, jsonify, redirect, url_for
 #Blueprint has many roots / URLs inside it

views = Blueprint(__name__, "views")



from flask import Blueprint

views = Blueprint(__name__ ,'views')

@views.route("/")
#this function will run, whenever we go to the /-route: ""
def home():
    return '<h1>Test</h1>'

