#
#"__" = makes website folder a python package


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import  path
# os = operating system

db = SQLAlchemy()
# this is the database object (above)
DB_NAME = "database.db"

def create_app(): 
  app = Flask(__name__)
#initializes application
  app.config['SECRET_KEY']='fjehrjd jewbhfj hwejfeui'
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
  # the f is a f-string 
  # My Sql-Alchemy-Database is stored at this (= f'...') location
  db.init_app(app)
  # this is going to take the database we defined here (db = SQLAlchemy   this is located in python app file init_)

  from .views import views
  from .auth import auth

  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')
  #url_prefix = is saying: all of the urls inside those blueprint files, how do I access them



  from .models import User, Note
  # reason for importing: we aren't going to use anything, but we need to make sure that this model.py-file runs, ...
  # by importing we are loading it
  # before we define and create our database

  # (we can't start a variable with ".")

  with app.app_context():
    db.create_all()

  return app









# here it could come up problems eventually

# version of tutorial
# def create_database(app):
  # is going to check wether the database already exists, and if not it is going to create it. If it does exist we
  # don't want override it, because it has already data in it
  if not path.exists('website/' + DB_NAME):
  # at first we check if the databse exists, if not:
    db.create_all(app=app)
    # we create database
    # app has SQL-Alchemy URI -> tells us where to create the database, +  we need to tell flask-SQL-Alchemy which
    # app we're creating the database for
    print('Created Database! ')

# I had a problem here with the part: app=app. The solution was: SQLAlchemy already wasn't going to override the database