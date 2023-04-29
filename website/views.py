from flask import Blueprint, render_template, request, jsonify, redirect, url_for
 #Blueprint has many roots / URLs inside it

views = Blueprint(__name__, "views")



@views.route("/")
#this function will run, whenever we go to the /-route: "http://127.0.0.1:5000/"
def home():
    return '<h1>Test</h1>'

