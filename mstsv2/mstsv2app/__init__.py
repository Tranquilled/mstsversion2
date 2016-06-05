from flask import Flask
from flask_restful import Api
from db import db




# Starts flask application
app = Flask(__name__)
app.config.from_object('settings')







# Initializes Flask SQLAlchemy
db.init_app(app)
db.app = app


# Uses Blueprint to import different modules
from blogs.routes import blogs_blueprint
from homepage.routes import homepage_blueprint


app.register_blueprint(homepage_blueprint,url_prefix='')
app.register_blueprint(blogs_blueprint,url_prefix='api/blogs')

db.create_all()
