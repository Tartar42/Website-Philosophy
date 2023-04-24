from flask import Flask
from views import views
#this will import the variable "views" (right) from the "views-file"

app = Flask(__name__)
#initializes application

app.register_blueprint(views, url_prefix="/views")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
#debug=True makes the website refresh on her own. So when we change things here, they're also changed in the website
