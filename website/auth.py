#here we are storing all the stuff for the authentication of users. Login page, etc.

from flask import Blueprint, render_template, request, flash #, jsonify, redirect, url_for
 #Blueprint has many roots / URLs inside it

auth = Blueprint("auth", __name__)

@auth.route('/login', methods=['GET', 'POST'])
#'Get', ...    =  strings for the type of requests that this route can accept / for the submit button to work 
def login():
  # data = request.form
    # request.form = request variable -> whenever u access this request inside of a route, it will have information about the request that was sent to acces this route
    #it will say the url, the method, infromation that was sent
    # we are going to access the form attribute of our request, which has all of the data that was sent as a part of a form
  # print(data)
    # the data is printed out in terminal
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>logout<p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        # using .get to get a specific attribute / value
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4: 
            flash('Hey! HEYYY! your email is too short.', category='error')
        elif len(firstName) < 2:
            flash('Hey! HEYYY! At least two letters bro', category='error')
        elif len(password1) < 6:
            flash('Hey! HEYYY! Your password is wayy to short buddy', category='error')
        elif password1 != password2:
            flash('Hey! HEYYY! type your password correctly', category='error')
        else:
            flash('Yep. Everything fine', category='success')
        #for checking if it's valid data (that people have typed in in all fields / rectangles + ...)
    return render_template("sign_up.html")