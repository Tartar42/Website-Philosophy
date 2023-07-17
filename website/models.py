from . import db
# means: from this package / dor / . / (init) import db (db = SQLAlchemy())
from flask_login import UserMixin
# a custom class that we can inherit, that will give our user object something specific for our flask login 
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True, default=func.now ))
    # Timezone info is also going to be stored. func.now -> gets the current date and time 
    # when we create a new note object, it will call func, it will get the time it is and it will use that to store
    # in the db.DateTime-Field + it will store the timezone info of this daytime object
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # this creates a relationship
    # 'user.id' -> user is referencing this class below, id is the field of this user-object

# important: all of our notes must belong to a user - association with user. We have to set up a relationship between
# this Note-Object with the User-Object -> Foreignkey

# just for user object: (..., UserMixin)
class User(db.Model, UserMixin):
# when u want to make a new database model / u want to store a differnt type of object , u are going to the define
# the name of the object (not plural).
# than u are going to have it inherit from db.Model
    id = db.Column(db.Integer, primary_key=True)
    # here we are cerating columns for our database
    # for all of our objects we have to have a primary key
    # in () we have the type of columns
    # ID = primary key
    email = db.Column(db.String(150), unique=True)
    # whenever u define a string u have to pick a maximum length, (150) for example
    # unique=Ture means: no user can have the same email
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    notes = db.relationship('Note')
    # tell flask: everytime we create a note add into this users note relationship that note-id
    # lowercase 'n' (for note) because in sql foreignkey has lowercase, and Class ist capital
# we will store all of our users like this


# we haven't created the database here. Just the modul.