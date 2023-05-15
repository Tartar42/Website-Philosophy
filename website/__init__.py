#
#"__" = makes website folder a python package

from flask import Flask

def create_app(): 
  app = Flask(__name__)
#initializes application
  app.config['SECRET_KEY']='fjehrjd jewbhfj hwejfeui'

  from .views import views
  from .auth import auth

  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')
  #url_prefix = is saying: all of the urls inside those blueprint files, how do I access them

  return app
